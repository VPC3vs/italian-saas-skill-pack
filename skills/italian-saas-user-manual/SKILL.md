---
name: italian-saas-user-manual
description: Create branded Italian-language user manuals for SaaS web apps, especially when the user wants an onboarding discussion first, product/company context inferred from a repository or running app, branding extracted from logos/fonts/color palette, a proposed length/tone/outline/sample paragraph for approval, and then a polished PDF manual only after approval.
---

# Italian SaaS User Manual

## Overview

Use this skill to produce a professional user manual in Italian for a SaaS web app. Treat the work as a two-phase process: first discover and agree on the manual, then generate and verify the final PDF.

## Non-Negotiable Flow

1. Discuss before producing.
2. Infer what can be inferred from the repo or running app.
3. Separate facts from assumptions.
4. Propose the manual plan in Italian.
5. Wait for explicit approval before generating the final PDF.
6. Render and visually verify the PDF before delivery.

Do not create the final PDF during the first pass unless the user has already approved the length, tone, structure, and sample content in the current conversation.

## Discovery

Inspect the available repository before asking broad questions. Prefer `rg --files`, then read likely sources such as:

- README, product docs, onboarding docs, and existing manuals.
- `package.json`, route files, app config, navigation, menus, page titles, translations, forms, and feature components.
- Public assets: logos, favicons, app icons, screenshots, CSS variables, theme files, Tailwind config, design tokens, and font declarations.
- Auth, role, tenant, billing, workflow, reporting, integration, import/export, notification, and admin screens.

If the app can be run locally, start the dev server, open it in a browser, and capture screenshots of representative screens. If credentials, seed data, or setup are missing, say so and continue from static repo evidence.

If the user gives a deployed URL, inspect the live app as the primary brand/reference source. Respect login boundaries and ask for access details only when necessary.

## Discussion Gate

Ask only for missing information that materially changes the manual. Keep questions concise. Useful topics:

- Company name, logo preference, and any mandatory legal/footer text.
- What the SaaS app does, primary user roles, and the main jobs users complete.
- Target audience: end users, admins, customers, internal staff, or a mix.
- Desired manual depth: quick start, standard user guide, admin guide, or complete manual.
- Tone: formale, amichevole, tecnico, istituzionale, operativo.
- Required sections, excluded features, screenshots, support contacts, and final filename.

When repo evidence conflicts with user answers, trust the user and mention the discrepancy briefly.

## Approval Proposal

Once there is enough context, respond in Italian with a compact proposal before generating files. Include:

- Assumptions and inferred facts, labeled clearly.
- Recommended length, such as "8-12 pagine" or "15-20 pagine".
- Recommended tone.
- Proposed table of contents.
- One representative paragraph in the proposed style.
- Any missing items that would improve the PDF but are not blocking.

End by asking for explicit approval or requested changes. Do not proceed to PDF generation until the user approves.

## Manual Content Standards

Write the manual in natural Italian. Prefer clear operational language over marketing copy. Use product-specific terms found in the app, but explain them the first time if they are not obvious.

Include only sections that fit the discovered product. Common SaaS sections are:

- Copertina.
- Sommario.
- Introduzione and purpose of the app.
- Accesso, account setup, password reset, and roles.
- Dashboard or home page orientation.
- Main workflows, one per major feature area.
- Search, filters, export, notifications, integrations, or settings when present.
- Admin or configuration tasks when relevant.
- Troubleshooting and support.
- Glossary if the product uses domain-specific terms.

Do not invent unsupported features, pricing, guarantees, compliance claims, or company policies. If the repo suggests a feature but behavior is unclear, describe it conservatively or ask.

## Branding

Extract branding from the app whenever possible:

- Use the app logo or favicon from public assets or the live app.
- Use the app font stack when available. Embed local font files only when present and suitable for PDF use.
- Build the color palette from CSS variables, theme config, design tokens, or computed browser styles.
- Use screenshots only when they are readable and relevant; crop away browser chrome and irrelevant whitespace.

If brand assets are incomplete, use a clean document layout inspired by the discovered palette and state what could not be found.

## PDF Generation

Choose the simplest reliable document route available in the environment:

- For layout-heavy manuals, create an HTML source and print/render it to PDF.
- For Word-style deliverables, create a `.docx` first, then export or render to PDF if supported.
- For simple manuals, a Markdown-to-PDF route is acceptable if branding and pagination remain professional.

Before final delivery, render the PDF pages to images and inspect them. Verify:

- Logo, colors, fonts, headings, page numbers, and table of contents render correctly.
- Italian text is not clipped or overlapping.
- Screenshots are legible.
- Page breaks do not split important headings from content.
- The final file opens and has the expected page count.

Fix visible layout problems before presenting the PDF path.

## Final Response

Keep the final response brief. Provide:

- The PDF path.
- The source file path if useful.
- Any important caveats, such as missing screenshots or unavailable brand fonts.
- The verification performed.
