---
name: italian-saas-demo-video
description: Create SaaS demonstration videos with a complete professional Italian script and female Italian voice-over. Use Graphify and Gravity to discover the app and select evidence-backed screen recordings. Adapt duration to the workflows being explained; 2-5 minutes is a preferred range, not a cap. Use for product demos and narrated SaaS walkthroughs, rather than written manuals or standalone speech.
---

# Italian SaaS Demo Video

Create a branded video that shows a real user completing useful work in a SaaS application, with synchronized female narration in professional Italian. Carry forward the discovery, branding, factual accuracy, and visual verification practices of `italian-saas-user-manual`.

The deliverable is a playable narrated video, accompanied by the complete Italian commentary. A script, storyboard, silent recording, or mock interface alone does not complete a video request. “Act the commentary” means voice-over performance; add an on-screen presenter only if requested.

## Discover the SaaS before choosing shots

Load `$gravity` and `$graphify` from the current skill catalog. They are explicit dependencies of this workflow. Gravity coordinates focused investigation and evidence review; Graphify maps the product. Follow their current instructions rather than copying their pipelines here. Keep discovery read-only with respect to application code and business data; local analysis and media artifacts belong within the task's authorized scope.

1. Resolve the supplied repository or app URL. Inspect repository instructions and available docs, then locate `graphify-out/graph.json` at the SaaS project root. Do not graph the unrelated working directory when the product lives elsewhere.
2. Query an existing graph first. Use its vocabulary, communities, source paths, and `EXTRACTED` edges to locate user roles, entry screens, core entities, and workflows. Treat `INFERRED` relationships as leads and `AMBIGUOUS` relationships as unresolved. Check relevant freshness signals; build or update only through the installed Graphify workflow and within authorized local artifact writes.
3. Use Gravity to divide discovery into independent read-only lanes only when useful, such as core workflows and role-dependent features. Give workers the relevant graph slice; retain one owner for the final recording plan. Simple apps need no swarm.
4. Confirm candidate workflows in the source and running UI. Prioritize routes, navigation labels, forms, validations, success states, permissions, and real reports or exports. Use `rg --files` and targeted reads to resolve gaps, not to substitute a menu inventory for a user journey.
5. Inspect the running app and record the exact route, role, starting state, actions, and observable result for each candidate scene. Graph connectivity identifies where to investigate; it does not prove that a feature works or deserves screen time.

Read [references/discovery-and-storyboard.md](references/discovery-and-storyboard.md) for focused graph questions, the scene evidence table, and duration planning.

For a live-only app, use authorized browser inspection and supplied product documentation. Use any supplied graph, but do not claim repository-level verification. If a required skill or graph capability is unavailable, name the gap, continue independent source/UI discovery, and resolve access only when it blocks a faithful recording. Never invent graph nodes or product behavior to fill gaps.

Use the application's logo, colors, typography, and terminology. Inspect brand assets, CSS variables, theme files, and actual screens. If user descriptions conflict with observed behavior, identify the discrepancy and reconcile it before demonstrating that behavior.

## Establish the brief and recording plan

Infer what the supplied app and conversation already establish. Ask only for missing details that change the demo: audience, main job to demonstrate, required workflows, role/account access, or a firm duration constraint. Use safe demo data and existing authorized demo/staging access.

Before production, present a compact proposal in Italian with:

- Product facts, assumptions, target audience, and the outcome viewers will see.
- Selected workflows and omitted features, with the reason for that scope.
- A scene table containing timing estimates, screen/action, full narration or a linked draft, and the observable outcome.
- Estimated duration and its rationale, plus a representative Italian narration passage and the chosen voice approach.

Respect a requested discussion-first or storyboard-approval workflow: prepare the reviewable plan and voice sample, then wait before final production. Reuse approval already present in the conversation. When the user has authorized end-to-end creation and the brief is sufficient, state the plan and continue without imposing a new approval gate.

## Let explanation determine duration

Treat **2-5 minutes as a preferred range, not a fixed default or hard maximum**. Choose the shortest duration that clearly demonstrates the selected jobs and their results. A complex SaaS may need longer; explain why. Do not stretch a simple app to fill time or compress essential explanation merely to hit five minutes.

Estimate time from real workflow steps, necessary context, UI reading time, and narration. Start around 130-150 spoken Italian words per minute with natural pauses, then use generated audio durations and recorded actions to set the final timeline. Do not infer duration from repository size, route count, or graph centrality alone.

If the user supplies a hard cap, prioritize one coherent journey and essential supporting features. State what is omitted instead of rushing the narrator. Propose chapters for a longer demo when they help navigation; do not create a series unless requested.

## Write and perform the Italian commentary

Write the entire spoken script in natural professional Italian before recording. Keep on-screen directions, evidence, and pronunciation notes separate from words to be spoken. Explain purpose, demonstrate the action, and state its visible result. Use short spoken sentences and exact product labels; explain necessary jargon once.

Favor a calm, confident, helpful tone over promotional superlatives. Avoid unsupported efficiency metrics, pricing, guarantees, integrations, or compliance claims. Demonstrate one coherent example with consistent fictional names and values.

Voice direction for a capable speech provider:

> Voce femminile adulta, italiano standard. Tono professionale, naturale e cordiale; autorevole senza enfasi pubblicitaria. Articolazione chiara e ritmo misurato. Usa pause brevi fra le istruzioni e lascia il tempo di osservare il risultato sullo schermo. Dai risalto alle azioni e ai benefici verificabili. Rispetta le pronunce concordate per marchi e sigle. Leggi soltanto il copione destinato alla voce.

Select an Italian female voice from the provider's actual available voices; audition it rather than guessing gender or accent from its name. Keep the same voice and delivery settings throughout. Use an available quality speech tool first. The bundled Windows helper is a local fallback; disclose its synthetic desktop-voice quality and do not describe it as a human or studio recording.

Generate and listen to a short representative sample containing the product name, a UI label, and any difficult acronym. Correct pronunciation, pauses, and pacing before rendering all scenes. Generate separate audio segments at natural sentence boundaries so retakes and synchronization remain manageable. Rewrite overlong speech before changing its speed.

## Record and assemble

Read [references/production.md](references/production.md) when preparing narration, footage, and final assembly. It documents the tested local helpers and their limits.

- Rehearse each workflow before capturing it. Start from the planned role and data state, hide credentials and irrelevant browser chrome, and show the resulting saved record, changed state, or report.
- Use actual app recordings with the available documented browser/capture tools. Prefer a readable 16:9 1080p presentation with deliberate cursor movement and restrained zooms. A screenshot-based walkthrough is a labeled alternative when recording is unavailable, not evidence of interactions that were never observed.
- Use demo records for mutations. A demo request does not by itself authorize sending invitations, messages, payments, publishing, deleting production records, or changing access. Stop before such an action unless it is already authorized; show a safe preview or another verified workflow when appropriate.
- Align narration to the action it describes. Let a result appear before discussing it. Remove dead loading time and repeated navigation while preserving understandable cause and effect. Use the actual speech duration to adjust shots; never cut off a sentence to meet an estimate.
- Use short branded opening/closing cards only where useful. Keep UI labels readable. Music is optional and off by default; if requested, use authorized music quietly under speech.
- Export an MP4 with H.264 video and AAC audio, plus the full Italian script. Create Italian SRT subtitles from the final narration when supported; validate their timing and line breaks. Do not present estimated word timings as verified alignment.

## Verify and deliver

Measure the actual exported duration and compare it with the brief. Confirm that the file contains both decodable video and audible narration. Review opening, closing, every scene transition, and all critical UI actions; play through the complete video and audio when the environment supports it.

Check that narration and actions agree, the chosen voice sounds female and Italian, pronunciation is correct, text is legible, no private data appears, and audio has consistent level without clipping. Inspect subtitle accents, timing, safe placement, and overlap if subtitles are included. Verify the visible end result of every demonstrated workflow against its evidence.

If playback or listening is unavailable, say precisely which verification was not possible. Do not equate successful encoding with professional delivery quality. Repair observed defects before final delivery.

Deliver `<product>-demo-it.mp4`, `<product>-copione-it.md`, and validated subtitles if produced. Keep source footage, per-scene audio, graph receipts, and the editing manifest in the task's work area; include editable production files when useful or requested. Follow the host's designated output directory.

The final response should link the video and script, report actual runtime and the voice used, summarize verification, and disclose material limitations. If access, capture, or voice generation prevents completion, deliver the usable draft assets with the exact blocker and next required input; never label a draft as a finished demo.
