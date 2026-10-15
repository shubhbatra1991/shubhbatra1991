# Commit Defender review

Prepared on `codex/commit-defender`. No commit, push, merge, permission change, or workflow execution on GitHub.

## Changes in this task

- README: replaces only the contribution snake picture with Commit Defender and its reduced-motion source.
- `.github/workflows/snake.yml`: retains the daily/manual/main triggers, existing `contents: write` permission and existing output-branch publisher. Replaces snake generation with checkout (credentials not persisted), standard-library Python tests and generator. The historical workflow filename is retained.
- `scripts/generate-commit-defender.py`: fetches the unauthenticated public GitHub calendar; preserves daily dates and activity levels. Does not fetch repository details, use a token, infer counts or invent activity. Invalid/incomplete data fails before publishing.
- `scripts/test-commit-defender.py`: four tests cover calendar fidelity, malformed data, static fallback and zero-activity handling. Synthetic fixtures exist only in tests, never in published graphics.
- `assets/games/commit-defender.svg` and `commit-defender-static.svg`: initial verified snapshots. Workflow-generated daily assets are published to `output`; these local snapshots are not automatically refreshed.

## Artwork and validation

Original pixel spacecraft, cyan energy beams, green activity cells and cyan/purple particles on an opaque navy panel. Four active dates are selected from the actual calendar. A synchronized 20-second loop restores every affected cell and returns the ship to its starting position. No game score or fabricated operational status. This is decorative animation, not an interactive game.

Snapshot source: https://github.com/users/shubhbatra1991/contributions — retrieved 2026-10-15, covering 369 days from 2025-10-12 to 2026-10-15. Levels match GitHub's public calendar; no counts are displayed. Publicly shown aggregate activity can include anonymized private contributions when the account enables that GitHub setting; no private repository names or details are fetched or exposed.

- Embedded-image browser captures confirmed ship movement, projectile travel and particle effects. Component fixtures accelerated the same animations to inspect effects separately; the final full image was also captured during its firing interval.
- Static control remained unchanged between frames. Static asset contains zero animation elements.
- Reduced-motion support: README picture selects static SVG; internal media query hides animated groups and shows a static ship. OS preference switching was not exercised in the browser test.
- Light/dark surrounding backgrounds and a 358 px image width checked locally. Intrinsic size 860 × 232; approximately 104 px tall at 390 px wide. Small date/source text is supplemental; meaningful calendar access remains the native GitHub link.
- Animated SVG approximately 58 KB; static approximately 48 KB. No scripts, external fonts/styles, filters, dependencies or raster payloads. Four generator tests pass; `git diff --check` passes. No formal CPU benchmark was run.

## Publication limitation

The README references the future `output/commit-defender.svg` and `output/commit-defender-static.svg` files. Those URLs will remain unavailable until an approved publication and successful workflow run. This task cannot truthfully verify live GitHub rendering or GitHub image caching before that happens. Local image rendering is verified; final on-GitHub animation, reduced-motion selection and caching require a post-publication check. Existing unrelated uncommitted profile changes are preserved.
