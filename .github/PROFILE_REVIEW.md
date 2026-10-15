# Compact profile review

Updated 14 October 2026. No push or publication performed.

## Technical Arsenal refinement — 15 October 2026

Branch: codex/technical-arsenal. No commit or push. Pre-existing README edits preserved.

Replaced the hidden skills table with six visible centered groups and 17 local Shields.io SVG badges (24 px display height). Badge labels, colors, and Simple Icons slugs are recorded in assets/badges/sources.json; downloads use https://img.shields.io/badge/{label}-{color}?style=flat&logo={slug}&logoColor=white. Azure, IndexedDB, LLM APIs and RAG use text-only badges; C# uses the .NET family icon. No invented logo artwork.

Evidence: React, TypeScript, Next.js and IndexedDB from the public DealPatch README/manifest; JavaScript from its public language listing; C#/.NET and Azure from the personal website; Node.js, PostgreSQL (FounderOS), Three.js and RAG from the previously reviewed public Projects page; LLM APIs from SignalOps-AI; Git/GitHub Actions from these public repositories. Unity is owner-confirmed. Python remains explicitly labeled exploring. C++, Docker, SQL Server, MySQL and Express were not established by the reviewed evidence and were omitted.

Two instances of the original assets/decorations/animated-divider.svg bracket the Arsenal and implementation notes. A cyan pulse traverses a thin line every seven seconds. SVG-contained CSS requires no JavaScript or README styles. Reduced-motion CSS hides the pulse, and the picture source selects static-divider.svg. Hero, project thumbnails, links and snake workflow are unchanged by this refinement.

Verification: GitHub Markdown API accepted the markup and retained picture sources and badge dimensions. Browser preview loaded every image; the divider transform changed between observations. All new SVGs parse successfully. The published main-branch hero SVG loads. New divider animation on the actual GitHub profile remains unverified until an approved publish; the published hero's blinking was not conclusively sampled in this run. Reduced-motion device selection and mobile layout need final GitHub review. No broken assets were found.

Before/after browser captures are provided in the chat. They use local assets; the after capture uses GitHub-rendered HTML with a local preview stylesheet. They are not screenshots of a published change.

## Previous compact-layout implementation

Hero and social links preserved. Featured projects use a two-column GitHub HTML table with 300 px 16:9 thumbnails, a title, one-line description, and GitHub / Live Demo links. Duplicate links below the cards are removed. Portfolio previews use the same compact table layout. Project Oven remains a short text entry; implementation notes stay collapsed. Contribution snake is visible by default.

## Real screenshot crops

Four new assets were cropped from the existing public screenshots, without stretching. Crops are expressed as left, top, right, bottom in original pixels:

- dealpatch-thumb.png: dealpatch-overview.png, (250, 80, 1370, 710), resized proportionally to 640 × 360.
- signalops-thumb.png: signalops-overview.jpg, (276, 582, 1236, 1122), resized proportionally to 640 × 360. Focus: demo metrics and event chart.
- personal-website-thumb.png: personal-website.jpg, (100, 70, 1220, 700), resized proportionally to 640 × 360.
- 3d-portfolio-thumb.png: 3d-portfolio.webp, (56, 2, 584, 299), retained at 528 × 297.

Removed the oversized dealpatch-card.png and signalops-card.png composites. Unused original screenshots and unreferenced dealpatch.png / signalops.png have been removed. The crop source names below are historical provenance, not files retained in the repository. The linked Review Queue screenshot is retained.

## Verification and limits

GitHub's POST /markdown API rendered the current README successfully and preserved both tables, image widths, relative sources, and picture sources. This verifies GitHub's renderer, not the final unpublished profile page.

Browser inspection of that returned HTML with local assets measured the featured table at 232.75 px tall and the portfolio table at 214.35 px. All images loaded. Both snake URLs returned HTTP 200; the live dark SVG's snake segment transforms changed between observations, confirming animation. The workflow is unchanged.

Final on-profile verification is pending publication because the new local thumbnail files do not yet exist on GitHub. Table cells remain side by side on narrow screens, as requested; unlike the previous inline cards, they do not stack. GitHub may shrink or horizontally scroll tables on phones.

Hero animation and reduced-motion variants are unchanged. Approved Unity gameplay media remains pending: assets/games/project-oven-gameplay.png and optional project-oven-gameplay.gif. No private source or credentials were copied.

## Sources and media provenance

Original screenshot filenames in this table record the source of the retained thumbnails; unused originals have been removed.

Only public pages/repositories and information explicitly supplied by the owner were used. No private repository was accessed or modified.

| Asset / claim | Evidence |
| --- | --- |
| Engineering positioning, React, TypeScript, Next.js, C#/.NET, APIs, Azure, conversational AI and LLM workflows | [Personal website](https://www.saurabhbatra.com/) |
| RAG, Node.js, Three.js and React Three Fiber | [Public Projects page](https://www.saurabhbatra.com/projects) |
| Python exploration, Unity focus | Owner's request; Python is presented as exploration, not attributed to the two featured apps |
| DealPatch features, stack and simulated AI boundary | [Public README](https://github.com/shubhbatra1991/dealpatch#readme) and [package manifest](https://github.com/shubhbatra1991/dealpatch/blob/main/package.json) |
| `assets/projects/dealpatch-overview.png` | Existing [public screenshot](https://github.com/shubhbatra1991/dealpatch/blob/main/documentation/Images/overview.png), copied unchanged |
| `assets/projects/dealpatch-review-queue.png` | Existing [public screenshot](https://github.com/shubhbatra1991/dealpatch/blob/main/documentation/Images/review-queue.png), copied unchanged |
| SignalOps features, stack and limitations | [Public README](https://github.com/shubhbatra1991/signalops-ai#readme) and [package manifest](https://github.com/shubhbatra1991/signalops-ai/blob/main/package.json) |
| `assets/projects/signalops-overview.jpg` | Actual [public demo](https://signalops-ai-nine.vercel.app/demo), captured in Dark / Teal appearance, guided-tour prompt dismissed; fictional demonstration data |
| `assets/projects/personal-website.jpg` | Actual [public website](https://www.saurabhbatra.com/), captured from the browser |
| `assets/projects/3d-portfolio.webp` | Existing public 3D Portfolio preview on the [Projects page](https://www.saurabhbatra.com/projects), copied unchanged. It is not a newly captured rendering of the live 3D scene |
| Project Oven Unity version | Owner explicitly confirmed a separate Unity version and requested gameplay media remain pending. The website currently describes a different Phaser/TypeScript version |
| Hero SVGs | Original vector artwork generated by `scripts/generate-hero.py`; decorative diagram, not a product screenshot |

Both project repositories were confirmed public through GitHub's public API. Their homepage links returned HTTP 200. The website and Projects page loaded in a browser after initial Vercel checkpoints. The 3D portfolio returned HTTP 200 and exposed chapter navigation, quick view, and 360 explore controls; its WebGL scene did not render correctly in the inspection browser. LinkedIn blocked automated inspection; the owner-supplied URL is retained and is also linked from the website.
