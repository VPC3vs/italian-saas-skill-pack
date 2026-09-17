# Italian SaaS Skill Pack

![A derpy MS Paint-style doodle of SaaS documentation and video narration, with a wonky dashboard, an open guide, and a googly-eyed presenter at a microphone](assets/saas-activity.png)

Three Codex skills for explaining SaaS applications in Italian: a branded user manual, a narrated product demo, and an Italian-first bilingual launch teaser. Start from the actual product, use its language and branding, and verify what the audience will read or watch.

## Included skills

| Skill | Deliverable | Workflow |
| --- | --- | --- |
| [italian-saas-user-manual](skills/italian-saas-user-manual/SKILL.md) | Branded Italian PDF manual | Inspect the app, propose the outline and style, obtain approval, then generate and visually verify the PDF. |
| [italian-saas-demo-video](skills/italian-saas-demo-video/SKILL.md) | Narrated MP4 and complete Italian script; validated subtitles when produced | Use Graphify and Gravity to select verified workflows, write the commentary, record the app, generate female Italian narration, and check the finished video. |
| [italian-saas-brag](skills/italian-saas-brag/SKILL.md) | Teaser MP4, poster e copy IT/EN | Concept e storyboard verificati, composizione Hyperframes, voce opzionale e controllo separato per lingua. |

The narrated demo length follows the explanation. **Two to five minutes is a preferred range, not a cap.** Complex workflows may need longer; simple apps should not be padded. Narration uses professional Italian and a female voice, with pronunciation and pacing reviewed before production.

## Brag — teaser di lancio / launch teaser

`italian-saas-brag` traduce [latent-spaces/brag](https://github.com/latent-spaces/brag) per GPT/Codex: italiano predefinito, inglese selezionabile e due versioni separate con `--lang both`. Mantiene il workflow originale completo: teaser da 15–25 secondi, sette toni, storyboard, Hyperframes, musica e SFX, beat sync, reattività audio, poster incorporato nel frame 0 e copy social. La voce resta facoltativa, con Kokoro tramite Hyperframes; per l’italiano viene selezionata una voce italiana dello stesso provider.

La guida principale è tradotta in italiano; il testo inglese completo è in [SKILL.en.md](skills/italian-saas-brag/SKILL.en.md). Tutti i riferimenti tecnici inglesi, gli script, le cinque tracce musicali, gli effetti sonori e i metadati originali sono conservati integralmente. Le sole aggiunte operative riguardano lingua IT/EN e risoluzione dei percorsi in Codex.

```text
Usa $italian-saas-brag per creare il video di lancio di questa app in italiano.
Usa $italian-saas-brag --lang both --voice --format vertical per due versioni IT/EN.
Use $italian-saas-brag --lang en --tone polished for an English launch teaser.
```

Hyperframes, Node.js e FFmpeg restano le dipendenze di produzione originali; il pack non installa questi runtime o le skill di dominio Hyperframes. L'analizzatore musicale originale include `pyproject.toml` e `uv.lock` per il percorso Python con `uv`. Sono inclusi gli asset audio originali, con i crediti e le note upstream conservati. [Audio e crediti](skills/italian-saas-brag/references/audio.md), [note originali della musica](skills/italian-saas-brag/assets/music/README.md).

## Install

Install the three skills with Codex's skill-installer. On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo VPC3vs/italian-saas-skill-pack --path skills/italian-saas-user-manual skills/italian-saas-demo-video skills/italian-saas-brag
```

On macOS or Linux:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" --repo VPC3vs/italian-saas-skill-pack --path skills/italian-saas-user-manual skills/italian-saas-demo-video skills/italian-saas-brag
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

The manual chooses an available PDF production route. No skill includes account credentials, production data, paid speech access, or a SaaS application. Use the product's authorized demo environment for recording actions.

## Repository layout

```text
assets/
  saas-activity.png
  saas-activity.prompt.md
skills/
  italian-saas-brag/
    SKILL.md
    SKILL.en.md
    LICENSE
    agents/openai.yaml
    references/
    scripts/
    assets/
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

The layout follows [gravity-swarm](https://github.com/VPC3vs/gravity-swarm): shared presentation assets at the root and installable skills under `skills/`. The manual and demo folders are preserved from their local source versions; Brag preserves its complete credited upstream resources with an Italian entrypoint and Codex path mapping.

## Validation

The original two skill folders were checked with skill-creator's `quick_validate.py`. Packaging checks cover local links, metadata, exact source copies, and archive integrity. Before packaging, the video helpers were exercised on Windows with female Italian speech generation, still/video input, mixed frame rates, non-square pixels, full MP4 decoding, output preservation, and a timing plan beyond five minutes.

The Brag translation is checked for skill structure, local references, installation parity and byte-for-byte preservation of every upstream file (the original entrypoint is retained as `SKILL.en.md`). A sample Hyperframes render is not part of its packaging validation.

These checks establish structure and helper behavior. Each real demo still needs review of its recorded actions, synchronization, pronunciation, voice quality, and exported playback. No benchmark or token-saving claim is made.

## Artwork and license

The banner was generated with the built-in image generation tool in deliberately derpy MS Paint style: wobbly outlines, flat colors, awkward proportions, and a googly-eyed narrator. Its symbolic dashboard is not a screenshot or evidence of a real product. The [generation prompt](assets/saas-activity.prompt.md) is included.

MIT licensed. See [LICENSE](LICENSE). Brag retains its upstream copyright and [MIT notice](skills/italian-saas-brag/LICENSE); original upstream audio is bundled with its existing credits and license notes; the code MIT notice does not replace the individual audio terms.
