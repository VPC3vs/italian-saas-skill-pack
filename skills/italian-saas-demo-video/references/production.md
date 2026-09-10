# Narration and video production

Read after choosing evidence-backed scenes. Discover tools at runtime: do not assume a recording API, installed browser, speech provider, or FFmpeg binary is available. Use installed tools and their current documentation. Keep source footage, narration segments, and intermediate encodes under the task's `work/` directory.

## Female Italian narration

Use a connected speech service when available and suitable for the requested quality. Discover its actual voice list and delivery controls, then apply the Italian voice direction from `SKILL.md`. Use existing authorized access; do not put credentials in scripts or ask for keys in chat. Send only the narration needed by the service. Use a generic narrator, not a cloned real person's voice.

When no suitable service is available, `scripts/narrate_windows.ps1` uses an installed, enabled `it-IT` female System.Speech voice. It lists/selects voices, reads UTF-8 plain text, and creates mono 48 kHz 16-bit PCM WAV. It fails if no matching voice exists or the output already exists. Desktop synthesis may sound mechanical; audition and disclose that limitation before calling the video polished.

Resolve `<skill-dir>` to this installed skill and choose real working paths:

```powershell
powershell.exe -NoProfile -File '<skill-dir>/scripts/narrate_windows.ps1' -ListVoices
powershell.exe -NoProfile -File '<skill-dir>/scripts/narrate_windows.ps1' -TextPath 'work/demo/01.txt' -OutputWav 'work/demo/01.wav' -VoiceName 'Microsoft Elsa Desktop'
```

Use the example voice only if returned by discovery. Omit `-VoiceName` for automatic selection of an enabled Italian female voice. `-Rate` accepts -4 through 4; start at 0 and assess the result. The helper accepts spoken text, not stage directions or SSML. Put pronunciation-oriented spellings in synthesis input and preserve standard product spelling in the readable script and subtitles.

Measure each WAV with Python's `wave` module: `getnframes() / getframerate()`. Convert other TTS formats to ordinary PCM WAV with FFmpeg before assembly. Keep sentences intact and match recorded actions to measured narration. Metadata cannot verify accent, naturalness, or pronunciation; listen to the audio.

## Footage preparation

Use the current browser/capture tool's supported recording method. Inspect supplied recordings before choosing cuts. Capture the relevant app surface and limit recording scope to it. Do not bypass browser tool restrictions through another automation mechanism.

Plan one main action or explanation per clip. Record enough setup and result hold to support the speech. Trim each clip to its intended starting state before assembly. If a click/result occurs at the wrong point, split or recut the clip; matching total duration alone does not synchronize the action.

If capture is unavailable, use screenshots only for a clearly described screenshot walkthrough or storyboard. Collect actual states through authorized interaction and do not fabricate transitions. If this materially changes the deliverable, obtain the user's preference while continuing the script and scene plan.

Brand cards and highlights may be simple code/vector overlays. Generated visuals must not replace real SaaS UI or prove unsupported features. Keep important screen text visible when cropping and scaling.

## Assemble prepared scenes

`scripts/assemble_demo.py` combines prepared video clips or still images with PCM narration WAVs. It needs Python 3 and FFmpeg with `libx264`, `aac`, `tpad`, and `loudnorm`. It discovers FFmpeg on PATH, then an installed `imageio_ffmpeg` runtime; `--ffmpeg` supplies an explicit executable. It performs no downloads or TTS requests.

Create a UTF-8 JSON manifest in `work/demo/`. Paths are relative to that manifest. Example:

```json
{
  "scenes": [
    {
      "title": "Panoramica",
      "visual": "01-dashboard.mp4",
      "audio": "01.wav",
      "lead_seconds": 0.3,
      "tail_seconds": 0.7
    },
    {
      "title": "Risultato del flusso",
      "visual": "02-result.mp4",
      "audio": "02.wav",
      "lead_seconds": 0.4,
      "tail_seconds": 1.0
    }
  ]
}
```

Only `visual` and `audio` are required per scene. Lead defaults to 0.3 seconds and tail to 0.5. Lead time is silence before narration while the visual already plays. Scene duration is narration plus lead/tail, rounded up to a video frame. If readable actions take longer than speech, allocate the extra time to lead/tail or split the shot to preserve the action and its result. The assembler holds the last frame of a shorter clip and trims longer footage: pre-align clips and ensure essential results appear before the cut. It drops source audio to avoid duplicate speech and captured notifications. Stills are held without simulated interactions.

```powershell
python '<skill-dir>/scripts/assemble_demo.py' 'work/demo/scenes.json' --output 'outputs/product-demo-it.mp4' > 'work/demo/timeline.json'
```

The output is 1920x1080, 30 fps H.264 with AAC narration. The helper preserves aspect ratio, pads unused space, joins PCM scene audio before the final AAC encode, and normalizes the complete voice track toward -16 LUFS with a -1.5 dB true-peak target. It does not overwrite existing deliverables. JSON output contains planned frame duration and per-scene speech offsets; measure the export separately for final runtime. There is no fixed duration cap.

The compositor does not capture the app, generate speech, correct pronunciation, synchronize individual clicks, create overlays, or align subtitles. Use an existing editor or targeted FFmpeg commands for those tasks. Do not turn the helper into a general editing system for a one-off effect.

## Verification and captions

Use FFprobe when available to inspect duration, streams, dimensions, and frame rate. Otherwise inspect FFmpeg input metadata and decode the export. In PowerShell, with `$demoFfmpeg` set to the discovered executable:

```powershell
& $demoFfmpeg -hide_banner -i 'outputs/product-demo-it.mp4'
& $demoFfmpeg -v error -xerror -i 'outputs/product-demo-it.mp4' -f null -
```

The metadata-only invocation intentionally has no output and may return a nonzero status; that is not the decode check. The second invocation must succeed. Extract representative frames and inspect them with an image viewer, then review real playback and audio where supported.

Build subtitles from the final script and real speech timings, preferably TTS word boundaries or a supported aligner. Scene offsets help place cues but do not establish word timing. Keep cues readable, usually one or two lines, break at natural phrases, and adjust against playback. If timing cannot be verified, label subtitles as a draft rather than synchronized.

Production references: [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html), [FFmpeg concatenation FAQ](https://ffmpeg.org/faq.html#How-can-I-concatenate-video-files_003f), and [System.Speech SpeechSynthesizer](https://learn.microsoft.com/en-us/dotnet/api/system.speech.synthesis.speechsynthesizer).
