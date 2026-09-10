#!/usr/bin/env python3
"""Join prepared SaaS footage and PCM narration; print scene timings as JSON."""

import argparse
import json
import math
import shutil
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

FPS = 30
STILLS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def find_ffmpeg(explicit):
    if explicit:
        return explicit
    found = shutil.which("ffmpeg")
    if found:
        return found
    try:
        import imageio_ffmpeg
    except ImportError as exc:
        raise ValueError("FFmpeg is unavailable. Supply --ffmpeg with an installed executable.") from exc
    return imageio_ffmpeg.get_ffmpeg_exe()


def prepare_scenes(manifest):
    data = json.loads(manifest.read_text(encoding="utf-8-sig"))
    if not data.get("scenes"):
        raise ValueError("The manifest needs at least one scene.")
    scenes = []
    cursor_frames = 0
    for index, scene in enumerate(data["scenes"], 1):
        visual = (manifest.parent / scene["visual"]).resolve(strict=True)
        audio = (manifest.parent / scene["audio"]).resolve(strict=True)
        with wave.open(str(audio), "rb") as wav:
            spoken = wav.getnframes() / wav.getframerate()
        if spoken <= 0:
            raise ValueError(f"Scene {index} has empty narration audio.")
        lead = round(float(scene.get("lead_seconds", 0.3)), 3)
        tail = float(scene.get("tail_seconds", 0.5))
        if not all(math.isfinite(x) and x >= 0 for x in (lead, tail)):
            raise ValueError(f"Scene {index} lead/tail durations must be finite and nonnegative.")
        frames = math.ceil((lead + spoken + tail) * FPS)
        start = cursor_frames / FPS
        scenes.append({
            "title": scene.get("title", f"Scena {index}"),
            "visual": str(visual), "audio": str(audio),
            "frames": frames, "lead_seconds": lead,
            "start_seconds": start, "end_seconds": (cursor_frames + frames) / FPS,
            "speech_start_seconds": start + lead,
            "speech_end_seconds": start + lead + spoken,
        })
        cursor_frames += frames
    return scenes, cursor_frames / FPS


def assemble(ffmpeg, scenes, output, scratch):
    def run(arguments):
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", *arguments], check=True)

    video_entries, audio_entries = [], []
    for index, scene in enumerate(scenes, 1):
        video = scratch / f"scene-{index:03d}.mp4"
        audio = scratch / f"scene-{index:03d}.wav"
        duration = scene["frames"] / FPS
        still_options = ["-loop", "1", "-framerate", str(FPS)] if Path(scene["visual"]).suffix.lower() in STILLS else []
        run([
            *still_options, "-i", scene["visual"], "-map", "0:v:0", "-an",
            "-vf", "setpts=PTS-STARTPTS,"
            "scale=w='trunc(min(1920,1080*dar)/2)*2':h='trunc(min(1080,1920/dar)/2)*2',"
            "setsar=1,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,tpad=stop_mode=clone:stop=-1",
            "-frames:v", str(scene["frames"]), "-c:v", "libx264", "-preset", "veryfast",
            "-crf", "18", "-pix_fmt", "yuv420p", "-n", str(video),
        ])
        lead_ms = round(scene["lead_seconds"] * 1000)
        run([
            "-i", scene["audio"], "-map", "0:a:0", "-vn", "-af",
            f"aresample=48000,adelay=delays={lead_ms}:all=1,apad,atrim=duration={duration:.9f}",
            "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", "-n", str(audio),
        ])
        # Generated basenames avoid concat-list quoting of user-supplied paths.
        video_entries.append(f"file '{video.name}'\n")
        audio_entries.append(f"file '{audio.name}'\n")
    video_list, audio_list = scratch / "video.txt", scratch / "audio.txt"
    video_list.write_text("".join(video_entries), encoding="utf-8")
    audio_list.write_text("".join(audio_entries), encoding="utf-8")
    run([
        "-f", "concat", "-safe", "1", "-i", str(video_list),
        "-f", "concat", "-safe", "1", "-i", str(audio_list),
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "1",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-n", str(output),
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--ffmpeg", help="Path to an installed FFmpeg executable")
    args = parser.parse_args()
    manifest = args.manifest.resolve(strict=True)
    output = args.output.resolve()
    if output.suffix.lower() != ".mp4":
        raise ValueError("The output must be an .mp4 file.")
    if output.exists():
        raise ValueError(f"Output already exists: {output}")
    scenes, duration = prepare_scenes(manifest)
    ffmpeg = find_ffmpeg(args.ffmpeg)
    output.parent.mkdir(parents=True, exist_ok=True)
    # TemporaryDirectory owns only its new child directory beside the work manifest.
    with tempfile.TemporaryDirectory(prefix="render-", dir=manifest.parent) as directory:
        assemble(ffmpeg, scenes, output, Path(directory))
    print(json.dumps({
        "output": str(output), "planned_duration_seconds": duration,
        "fps": FPS, "scenes": scenes,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, wave.Error, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
