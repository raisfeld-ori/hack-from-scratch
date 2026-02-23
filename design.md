# Design Spec — Hack From Scratch

## Goals
- Soft, game-like 80s vibe with a blue-forward palette.
- All primary pages must fit within 100vh with no vertical scrolling.
- Typography: retro headline + readable body.
- UI should feel calm, not harsh. Rounded corners, soft shadows, and gradients.

## Typography
- Headline: Press Start 2P
- Body: VT323
- Keep letter spacing subtle; avoid heavy glow.

## Color Palette
- Background base: deep navy / midnight blue
- Accent: soft sky blue to periwinkle gradients
- Text: pale ice blue / off-white

Suggested hex references:
- #0b1220 (base)
- #14233c (mid)
- #0a1526 (deep)
- #8fd1ff (light accent)
- #5c8dff (accent)
- #e9f2ff (text)

## Layout Rules
- Use CSS grid for compact, balanced cards.
- Avoid large vertical gaps; prefer 0.6–1rem.
- Ensure critical actions remain above the fold.

## Buttons
- Primary CTA: full-width when used in cards.
- Rounded, soft gradient, slight elevation.
- Uppercase text with moderate letter spacing.

## Main Page (Home)
Reference: [src/templates/index.html](src/templates/index.html)
Reference: [src/static/css/default.css](src/static/css/default.css)

Layout:
- Header with title + subtitle.
- Two info cards (Explanation, Please remember).
- Action card with Start level 0 and flag input.

Key elements:
- Explanation card includes the full-width “How it works” button.
- No visible scrollbar at 100vh.

## Info Page (How It Works)
Reference: [src/templates/info.html](src/templates/info.html)
Reference: [src/static/css/default.css](src/static/css/default.css)

Layout:
- Compact grid with 4 info cards + action area.
- Interactive details via HTML details/summary.
- Include flag SVG examples.

## Constraints
- Must fit 100vh at typical laptop resolutions.
- Keep text concise to avoid overflow.
- Use soft gradients, avoid neon-heavy styling.

## Notes for Future Updates
- If adding sections, reduce text length or tighten spacing.
- Prefer adding interactive elements (details, tooltips) instead of long paragraphs.
