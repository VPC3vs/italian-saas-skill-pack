# Italian SaaS Skill Pack

![A hand-painted scene of SaaS documentation and video narration, with a software dashboard, an open guide, and a presenter at a microphone](assets/saas-activity.png)

Two Codex skills for explaining SaaS applications in Italian: a branded user manual and a narrated product demo. Start from the actual product, use its language and branding, and verify what the audience will read or watch.

## Included skills

| Skill | Deliverable | Workflow |
| --- | --- | --- |
| [italian-saas-user-manual](skills/italian-saas-user-manual/SKILL.md) | Branded Italian PDF manual | Inspect the app, propose the outline and style, obtain approval, then generate and visually verify the PDF. |
| [italian-saas-demo-video](skills/italian-saas-demo-video/SKILL.md) | Narrated MP4 and complete Italian script; validated subtitles when produced | Use Graphify and Gravity to select verified workflows, write the commentary, record the app, generate female Italian narration, and check the finished video. |

The video length follows the explanation. **Two to five minutes is a preferred range, not a cap.** Complex workflows may need longer; simple apps should not be padded. Narration uses professional Italian and a female voice, with pronunciation and pacing reviewed before production.

## Install

Install both skills with Codex's skill-installer. On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo VPC3vs/italian-saas-skill-pack --path skills/italian-saas-user-manual skills/italian-saas-demo-video
```

On macOS or Linux:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo VPC3vs/italian-saas-skill-pack --path skills/italian-saas-user-manual skills/italian-saas-demo-video
```

The installer refuses an existing destination. If a skill is already installed, review and back up that version outside skill discovery directories before replacing it. A custom Codex installation may keep the system installer elsewhere; use its actual path.

## Use

Provide an accessible SaaS repository, running app URL, or relevant product materials.

```text
Usa $italian-saas-user-manual per creare il manuale utente di questa
applicazione. Analizza il prodotto e il branding, poi proponi indice,
lunghezza, tono e un paragrafo di esempio prima di generare il PDF.
```

```text
Usa $italian-saas-demo-video per creare una demo di questa applicazione.
Usa Graphify e Gravity per capire cosa registrare. Scrivi il copione e
realizza la narrazione con voce femminile professionale in italiano.
Adatta la durata ai flussi da spiegare: 2-5 minuti sono una preferenza,
non un limite. Procedi fino al video finale usando l'accesso demo fornito.
```

The manual keeps its proposal-and-approval workflow. The video respects a requested storyboard review and reuses approval already given; a sufficiently specified end-to-end request does not add another approval gate.

## Product evidence and dependencies

The demo skill depends on the separately installed **Graphify** and **Gravity** skills. They are not bundled here. [Gravity is published separately](https://github.com/VPC3vs/gravity-swarm); follow the installed Graphify skill for its supported setup and graph commands.

Existing graph relationships guide investigation. Current source and the running UI establish what can actually be shown, including role restrictions and deployment differences. Stale or inferred relationships are not proof of an available feature. With a live-only app, the skill records the limits of its source/UI evidence.

Recording requires accessible app screens and a supported capture tool. Speech requires a suitable available voice provider. The bundled [Windows narration helper](skills/italian-saas-demo-video/scripts/narrate_windows.ps1) can use an installed Italian female System.Speech voice; this is a synthetic desktop fallback, not a studio recording. The [assembly helper](skills/italian-saas-demo-video/scripts/assemble_demo.py) combines prepared footage and PCM WAV narration using Python and FFmpeg, producing 1080p H.264/AAC MP4. It can discover an installed `imageio_ffmpeg` runtime.

The manual chooses an available PDF production route. Neither skill includes account credentials, production data, paid speech access, or a SaaS application. Use the product's authorized demo environment for recording actions.

## Repository layout

```text
assets/
  saas-activity.png
  saas-activity.prompt.md
skills/
  italian-saas-user-manual/
    SKILL.md
    agents/openai.yaml
  italian-saas-demo-video/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
.gitignore
LICENSE
README.md
```

The layout follows [gravity-swarm](https://github.com/VPC3vs/gravity-swarm): shared presentation assets at the root and installable skills under `skills/`. These two skill folders are preserved from their local source versions.

## Validation

Both skill folders were checked with skill-creator's `quick_validate.py`. Packaging checks cover local links, metadata, exact source copies, and archive integrity. Before packaging, the video helpers were exercised on Windows with female Italian speech generation, still/video input, mixed frame rates, non-square pixels, full MP4 decoding, output preservation, and a timing plan beyond five minutes.

These checks establish structure and helper behavior. Each real demo still needs review of its recorded actions, synchronization, pronunciation, voice quality, and exported playback. No benchmark or token-saving claim is made.

## Artwork and license

The banner was generated with the built-in image generation tool as a gouache-and-watercolor illustration of SaaS documentation and narration. Its symbolic dashboard is not a screenshot or evidence of a real product. The [generation prompt](assets/saas-activity.prompt.md) is included.

MIT licensed. See [LICENSE](LICENSE).
