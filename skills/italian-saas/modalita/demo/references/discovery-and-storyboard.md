# From product evidence to a recording plan

Read the installed Graphify and Gravity skills first. Use their current commands and model controls. This reference adds the demo-specific questions and decisions; it does not replace those skills.

## Graph and source discovery

Resolve the supplied SaaS project root before checking `graphify-out/graph.json`. Query the existing graph with terms taken from its actual labels and communities; Graphify does not automatically translate Italian questions into English code identifiers. A suitable investigation may ask:

- Which user roles and entry routes start the main job?
- Which screens, forms, and entities connect its beginning to a useful saved result?
- Where are permissions, plan restrictions, or required setup enforced?
- Which reporting, search, export, or integration features support that job?
- Which UI components or routes expose those capabilities in the recorded deployment?

Use a broad neighborhood query for feature discovery and a focused path/DFS query for a workflow's dependencies. Preserve graph node IDs, edge evidence class, and `source_location` in the internal notes. Read the relevant files and verify the corresponding UI before turning findings into narration.

For read-only CLI queries, set `GRAPHIFY_QUERY_LOG_DISABLE=1`. Direct JSON inspection is also valid. Keep vocabulary expansion in memory. Do not invoke write-producing `save-result`, `reflect`, hooks, installs, or exports as a side effect of read-only discovery.

Treat `.needs_update`, a mismatched build commit, and relevant dirty/newer files as stale signals. Build or update a graph only when the installed Graphify workflow and current authorization permit local analysis artifacts. If that is unavailable, record the source/UI fallback and uncertainty. A graph relationship, even `EXTRACTED`, does not establish that the deployed feature is enabled for the intended account.

For a live-only product, inspect the accessible routes and supplied docs with permitted tools; use any supplied graph without inventing source locations. Do not graph this skill's files or the user's unrelated workspace to manufacture product evidence.

Gravity may assign substantial independent read-only lanes, such as the core user journey and admin/role restrictions. Give workers relevant graph slices and precise evidence targets; the coordinator integrates their findings and chooses scenes. Follow Gravity's actual model/effort requirements and report unavailable controls truthfully. Avoid multiple agents repeating the same repository tour.

## Scene evidence table

Keep an editable table in the working storyboard. Use one row per meaningful scene or beat; split a long scene into timed shots when needed.

| Field | What to record |
| --- | --- |
| User job and outcome | Why this scene belongs in the demo; the result the audience should understand |
| Role and starting state | Account role, tenant, prerequisite records, and relevant permissions |
| Screen and actions | Actual route, visible labels, reproducible action sequence, capture start/end states |
| Visible result | Saved record, status transition, filtered view, report, or another observable outcome |
| Evidence | Graph node/path and source location; current UI observation; unresolved differences |
| Spoken commentary | Complete Italian text, separate from capture directions and pronunciation notes |
| Timing | Word estimate, rehearsal time, then measured speech and final shot duration |
| Recording readiness | Ready, access missing, unsafe live side effect, or behavior still unverified |

Keep evidence in production notes, not as architectural narration in the public demo. Prefer a main journey with a few supporting capabilities over a tour of every menu. Do not pick scenes merely because their components have high centrality or many routes.

Show role changes explicitly if both user and admin views are relevant. Do not imply that a standard user can perform admin actions. When a feature is missing from the deployed app despite appearing in source, omit it or state its availability accurately; do not invent the screen.

## Duration estimate

This skill's preferred window is 2-5 minutes and may be exceeded when a clear explanation needs more time. There is no mandatory three-minute default and no need to pad an unusually simple demo to two minutes.

1. Select the jobs that the audience needs to understand.
2. Draft the full script and rehearse the actions. Estimate speech at roughly 130-150 Italian words per minute.
3. For each scene, use the longer of intelligible speech time and readable action time, with brief settling/result holds. Speech and actions normally overlap; do not add both durations as if they happen sequentially.
4. Sum scene lengths and any short opening/closing. Explain what drives the estimate, especially when it exceeds five minutes.
5. Replace estimates with measured generated audio and prepared footage. Trim repetition before speeding up speech. Preserve essential visible results.

Example of a proposal phrasing, to adapt only after real discovery: “La demo segue un flusso completo e mostra due funzioni di supporto. La durata stimata è di circa sei minuti, perché occorre distinguere il ruolo operativo dall'approvazione del responsabile. Il montaggio definitivo sarà basato sui tempi della voce e delle azioni registrate.” This is a writing example, not a claim about the user's application.

If a later request sets a strict time limit, obey it by narrowing scope and naming the omissions. Otherwise choose completeness and a natural pace over an arbitrary timestamp.
