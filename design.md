# Design Specification — Hack From Scratch

## Overview
Complete design documentation for all 5 CTF levels + transitions, components, and styling system.

**Current Version**: 2.0 (Updated Feb 2026)
- Page transition component added
- Level 5 complete Facebook redesign
- All 5 levels fully implemented and designed
- Modal system standardized
- Color palettes documented

## Goals & Aesthetic
- **Primary Theme**: Matrix-inspired hacker aesthetic (Levels 0-4: Dark blue retro)
- **Boss Level**: Modern white Facebook-style (Level 5)
- **Vibe**: Soft 80s/90s retro with professional security training focus
- **Constraint**: All pages fit 100vh (no vertical scrolling except L5 center feed)
- **Progression**: HTML inspection → Network tab → Parameter tampering → IDOR → Social engineering
  
## Typography

**Fonts**:
- Headlines: `Press Start 2P` (Google Fonts) - pixelated, retro
- Body/Code: `VT323` (Google Fonts) - monospace terminal feel

**Sizing & Spacing**:
- Titles: `clamp(1.4rem, 3.2vw, 2.4rem)` responsive
- Subtitles: 0.85–0.95rem
- Body: 0.88–0.95rem
- Letter spacing: Titles 1.5px | Subtitles 1px | Code 0.5px
- Line height: Body 1.3–1.5

## Color System

### Primary Palette (Levels 0-4)
```
| Element        | Hex       | RGB            | Usage               |
|----------------|-----------|----------------|---------------------|
| Deep Navy      | #0b1220   | (11, 18, 32)   | Main background     |
| Midnight       | #14233c   | (20, 35, 60)   | Cards, secondary bg |
| Deep Night     | #0a1526   | (10, 21, 38)   | Gradient deep point |
| Sky Blue       | #8fd1ff   | (143, 209, 255) | Primary accent      |
| Periwinkle     | #5c8dff   | (92, 141, 255) | Secondary accent    |
| Ice Blue       | #e9f2ff   | (233, 242, 255) | Primary text        |
| Off-white      | #f4fbff   | (244, 251, 255) | Highlights          |
```

### Level 5 Palette (Light Theme)
```
| Element        | Hex       | RGB            | Usage                  |
|----------------|-----------|----------------|------------------------|
| White          | #ffffff   | (255, 255, 255) | Main background        |
| Light Gray     | #f9fafb   | (249, 250, 251) | Input backgrounds      |
| Border Gray    | #e5e7eb   | (229, 231, 235) | Subtle borders         |
| Text Dark      | #1f2937   | (31, 41, 55)   | Body text on light     |
| Blue           | #3b82f6   | (59, 130, 246) | Buttons, accents       |
```

### Accent Colors
- Admin badge: `#dc2626` (red)
- User badge: `#1e40af` (dark blue)
- Matrix green: `#08f193` (scanlines)

## Layout & Grid

**Base Container**: 1040px max, 94vw responsive
**Grid System**: 12-column CSS Grid
**Card Layout** (Standard Levels):
- Mission card: 7 columns (left)
- Video card: 5 columns (right)
- Submit card: 3col offset, 8col span (centered bottom)

**Padding & Gaps**:
- Page padding: 1.35rem 1.25rem 1.15rem
- Card gap: 0.5–1rem (compact)
- Card padding: 0.8–1.2rem

**Responsive Breakpoints**:
| Width | Change |
|-------|--------|
| 1024px | Hide L5 left sidebar |
| 900px  | Grid → 2-column |
| 768px  | Grid → 1-column |
| 640px  | Minimal padding, stack |

**Level-Specific CSS Classes**:
- `.level-0-page`: Standard sizing
- `.level-1-page`: Compact - `padding: 0.6rem 0.75rem 0.55rem; gap: 0.5rem`
- `.level-2-page`: Matches Level 1
- `.level-3-page`: More compact - `padding: 0.52rem 0.65rem 0.48rem; gap: 0.42rem`
- `.level-4-page`: Compact sizing
- `.level-5-body`: Facebook layout (3-column fixed header)

## Components

### Page Transition (NEW)
**Location**: `src/static/css/default.css` (lines ~1-60)

**CSS**:
```css
.page-transition { position: fixed; z-index: 9999; display: none; }
.page-transition.start { animation: transitionCover 0.5s ... forwards; }
.page-transition.end { animation: transitionReveal 0.5s ... forwards; }
```

**Animations**:
- **Start**: scaleY(0 → 1) - covers page from top
- **End**: scaleY(1 → 0) - reveals page from top
- **Duration**: 0.5s cubic-bezier(0.4, 0, 0.2, 1)
- **Visual**: Blue→navy gradient + matrix green scanlines
- **Pseudo-element**: `::before` with repeating horizontal stripes

**JavaScript**:
- Intercepts all internal links
- Triggers `.start` class → 500ms delay → navigates → loads new page
- New page automatically gets `.end` class → reveals
- Result: Seamless, continuous transition

**Applied To**: All templates (index, info, level-0 through level-5, level-lock)

### Modal System
**Used In**: Level 4 (responses), Level 5 (profiles + flag)

**HTML Structure**:
```html
<div id="..." class="modal-overlay">
  <div class="modal-box">
    <div class="modal-header">Title × Button</div>
    <div class="modal-body">Content (scrollable)</div>
  </div>
</div>
```

**CSS**:
- `.modal-overlay`: Fixed full-screen, z-index 2000, `display: flex/none`
- `.modal-box`: White bg, max 450px width, centered
- `.modal-header`: Title + close button (×)
- `.modal-body`: Content area, scrollable if tall

**JavaScript**: `element.style.display = 'flex'` to show, `'none'` to hide

### Buttons

**Primary CTA** (`.cta-button.primary`):
- Full-width in cards
- Gradient: Cyan → darker blue
- Padding: 0.7–0.8rem
- Rounded: 8–12px
- Text: Uppercase, VT323, letter-spacing 1px
- Hover: translateY(-2px), enhanced shadow
- Font size: 0.85rem

**Challenge Button** (`.challenge-btn`):
- Gradient: #3b82f6 → #2563eb
- Padding: 0.7rem 1.4rem
- Hover: translateY(-2px), shadow 0 6px 16px rgba(...)
- Active: scale(0.98)
- Transition: 0.2s ease

**Hint/FAB Button** (`.hint-button`, `.fab-button`):
- 44px or circular
- Fixed positioning (bottom-right)
- Toggles overlay when clicked

### Video Embed
- Aspect ratio: 56.25% (16:9)
- Container: `.video-embed` with padding-bottom trick
- Iframe: 100% width/height inside
- Rounded: 8px
- Shadow: Soft drop shadow

### Cards
- Class: `.level-card`, `.level-grid`
- Grid-based layout
- Soft shadow
- Rounded corners
- Subtle borders
- Gap: 0.5–1rem

### Text Elements
- **Titles**: Press Start 2P, glow shadow, off-white
- **Subtitles**: VT323, sky blue
- **Body**: VT323, ice blue, 1.3–1.5 line-height
- **Code Pills**: Monospace, subtle bg, 0.4rem padding, 4px radius

## Pages & Levels

### Home Page (`index.html`)
**Structure**:
- Header: Title "Hack From Scratch" + subtitle
- Explanation card: CTF intro + "How it works" link
- Remember card: Safety guidelines
- Actions: Start Level 0 button + flag input area

**Features**: Full page transition support

### Info Page (`info.html`)
**Structure**:
- Title: "How It Works"
- 4 Info cards: What is CTF?, How it works, Safety, Pro tips
- Action buttons: Start Level 0, Back to home

**Features**: Expandable details, flag examples

### Level 0 — HTML Inspection
**File**: `src/templates/levels/level-0.html`

**Concept**: Learn DevTools, inspect HTML, find hidden flag in comment

**Layout**:
- Mission card (7col): "Open DevTools → Search for 'flag' → Copy and submit"
- Video card (5col): YouTube tutorial on DevTools
- Submit card (centered): Flag input form

**Challenge**: Find `<!-- Congrats! You found me. The flag is "CTF(ilovehtml)" -->`

**Elements**:
- `.level-ref-grid`: Where to look card + Common format card
- `.code-pill`: Example flag format
- `.form-error`: Red error if wrong
- `.level-tip`: F12 / Right-click Inspect hints

**CSS Class**: `.level-0-page` (standard sizing)

### Level 1 — Network Interception
**File**: `src/templates/levels/level-1.html`

**Concept**: Intercept requests via DevTools Network tab

**Layout**: Same as Level 0, compact sizing

**Challenge Button**:
- Blue → green on click
- Visual feedback for 1 second
- Simulates "capturing" a request
- Reverts to blue after timeout

**Key Elements**:
- `.challenge-btn`: Main button
- Network tab hints

**CSS Class**: `.level-1-page` (compact sizing)

### Level 2 — Admin Interception
**File**: `src/templates/levels/level-2.html`

**Concept**: Intercept admin requests (with hints)

**Layout**: Info cards + hint modal

**Hint System**:
- Floating button (44px, ?) bottom-right
- Opens modal/drawer with step-by-step hints
- Cannot see admin badge on posts (discovery aspect)

**Key Elements**:
- `.hint-button`: Floating help
- `.hint-drawer`: Modal overlay
- User posts without badges

**CSS Class**: `.level-2-page` (compact, matches L1)

### Level 3 — Parameter Tampering
**File**: `src/templates/levels/level-3.html`

**Concept**: Modify URL parameters to access admin data

**Layout**: Compact mission + video + submit

**Challenge** (5 steps):
1. Open DevTools
2. Look at URL
3. Find ID parameter (shows `?id=21`)
4. Change to ID 25 (admin)
5. Get flag

**Elements**:
- `.level-list`: Numbered steps
- URL structure hints
- No reference cards (difficulty ↑)
- No badges visible

**Backend**: `src/levels/level-3/level.py`
- `/myinfo?id=21` → User data
- `/myinfo?id=25` → **Admin flag**

**CSS Class**: `.level-3-page` (more compact)

### Level 4 — IDOR (Indirect Object Reference)
**File**: `src/templates/levels/level-4.html`

**Concept**: Access other users' data by modifying IDs in requests

**Layout**: Standard grid with 3 challenge buttons

**Challenge Buttons**:
1. "Your Info" (ID 21) → Normal user data
2. "Admin Info" (ID 25) → **Returns flag**
3. "List All" → All users JSON

**Response Modal**:
- `.response-modal`: Dark container
- Monospace font (VT323)
- Scrollable content
- Close button
- Professional code appearance

**Elements**:
- `.challenge-btn`: Each button with onclick
- `.response-modal`: API response display
- SVG close button

**Backend**: `src/levels/level-4/level.py`
- `GET /admin` → Admin flag
- `GET /users` → All users
- `GET /myinfo` → Your info

**CSS Class**: `.level-4-page` (compact)

### Level 5 — Social Engineering (Boss Level)
**Files**: `src/templates/levels/level-5.html` + `src/static/css/facebook.css`

**Concept**: Identify admin on fake Facebook platform

**Aesthetic**: White modern theme (unlike dark blue Levels 0-4)

**Layout**: 3-column Facebook-like
```
┌─────────────────────────────────────────────────┐
│  Fixed 60px Header (Level 5 • Social Eng)      │
├──────────┬──────────────────────────┬───────────┤
│ Left     │ Center Feed              │ Right     │
│ Nav      │ (Scrollable Posts Only)  │ Sidebar   │
│ 200px    │ 1fr flex                 │ 280px     │
│          │                          │           │
├──────────┼──────────────────────────┼───────────┤
│ • Profile│ Welcome post             │ 📊 Users  │
│ • Friends│ User posts:              │ 🎯 Tasks  │
│ • Feed   │  - Alice                 │ [Submit]  │
│          │  - Bob                   │           │
│          │  - Ariel                 │           │
│          │  - Yogev (ADMIN)         │           │
└──────────┴──────────────────────────┴───────────┘
```

**CSS Classes**:
- `.boss-level-header`: Fixed white header
- `.boss-facebook-layout`: 3-col grid
- `.boss-left-sidebar`: Nav, 200px fixed
- `.boss-center-feed`: Posts, scrollable
- `.boss-right-sidebar`: Info, 280px fixed
- `.fb-post`: Post cards
- `.fb-post-avatar-img`: User image
- `.fb-btn-view`: Profile button

**Components**:

**Header** (`.boss-level-header`):
- Fixed top, 60px height
- White gradient bg
- Title + subtitle

**Left Sidebar** (`.boss-left-sidebar`):
- Nav: Your Profile, Friends, Feed (emoji)
- 200px fixed width

**Center Feed** (`.boss-center-feed`):
- Welcome post (instructions)
- User posts (loaded via JS)
- **ONLY this scrolls** (not page)

**Right Sidebar** (`.boss-right-sidebar`):
- Active users count
- Task checklist (emoji)
- Submit Flag button

**Post Cards** (`.fb-post`, `.user-post`):
- Avatar: Image or initial fallback
- User: Name + @username
- Bio: Text content
- Button: "View Full Profile"

**Profile Modal** (`.modal-overlay`):
- Large avatar (90px circular)
- Name, username (@handle)
- Bio in gray box
- **ID** (essential for finding admin)
- Close buttons (top + bottom)
- **No admin/user badges** (no hints)

**Flag Modal** (`.modal-overlay`):
- Title: "Submit Your Flag"
- Light-themed input (white/gray)
- Blue submit button
- Error message (if wrong)

**Users** (from `src/levels/level-5/level.py`):
```python
{
  "id": 22, "name": "Alice", "username": "Alice",
  "image": "https://i.pravatar.cc/150?img=1", "isAdmin": False
},
{
  "id": 23, "name": "Bob", "username": "Bob",
  "image": "https://i.pravatar.cc/150?img=2", "isAdmin": False
},
{
  "id": 24, "name": "Ariel", "username": "Ariel",
  "image": "/static/images/ariel.png", "isAdmin": False
},
{
  "id": 25, "name": "Yogev", "username": "Yogev",
  "image": "https://i.pravatar.cc/150?img=4", "isAdmin": True
}
```

**JavaScript** (`loadUsersPosts()`):
- Fetches `/level-5/users`
- Creates post elements dynamically
- Adds click listeners to profile buttons
- Tests images, falls back to initials

**Challenge**:
1. View all user profiles
2. Find Yogev (ID 25)
3. Identify as admin (only by checking IDs)
4. Submit flag: `CTF(YourNowAnAmatuerHacker)`

**Key Insight**: No admin badges visible → must explore all profiles to find admin

### Level-Lock Page (`level-lock.html`)
**Purpose**: Prevent level skipping

**Layout**:
- Centered form
- Title: "Flag required"
- Message: Paste previous flag
- Input: Flag text
- Submit button

**Flow**: POST → validate → redirect or error

## Animations & Transitions

### Page Transition
- **Trigger**: Click internal link
- **Start**: `.page-transition.start`
  - Animation: `transitionCover` 0.5s
  - Transform: `scaleY(0 → 1)` (top to bottom cover)
  - Origin: top
- **Delay**: 500ms (while covering)
- **Navigation**: Happens during cover
- **End**: `.page-transition.end` (on page load)
  - Animation: `transitionReveal` 0.5s
  - Transform: `scaleY(1 → 0)` (top to bottom reveal)
- **Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` (smooth decel)
- **Result**: Seamless, continuous transition

### Button Interactions
- **Hover**: `translateY(-2px)` + shadow boost
- **Active**: `scale(0.98)` for press effect
- **Challenge (L1)**: Color toggle blue ↔ green (1s)
- **Duration**: 0.2s ease

### Modal
- **Display**: `display: none/flex` (instant)
- **Backdrop**: Semi-transparent overlay appears

## CSS File Organization

### `src/static/css/default.css` (~1680 lines)
**Sections**:
- **Lines 1-60**: Page transition component
- **Lines 61–150**: Global styles, typography, body
- **Lines 151–300**: Hero, titles, subtitles
- **Lines 301–600**: Grid system, card layout
- **Lines 601–800**: Button styles (CTA, challenge, etc)
- **Lines 801–1000**: Level 0–3 specific styles
- **Lines 1001–1200**: Level 4 styles (response modal)
- **Lines 1201–1400**: Level 5 boss styles (layout, header, sidebar)
- **Lines 1401–1500**: Modal system (`.modal-*` classes)
- **Lines 1501–1680**: Responsive breakpoints

### `src/static/css/facebook.css` (~470 lines)
**Content**:
- Post card styling (`.fb-post`, `.user-post`)
- Avatar styling (`.fb-post-avatar-img`, fallback initial)
- Sidebar specific (`.boss-left-sidebar`, `.boss-right-sidebar`)
- Facebook color variables
- Layout grid
- Button overrides for L5

## Accessibility
- ✅ WCAG AA color contrast (4.5:1 minimum)
- ✅ Focus states: Visible outline/shadow on buttons
- ✅ Semantic HTML (header, main, nav)
- ✅ Alt text on images
- ✅ Keyboard navigation (Tab through interactive)
- ✅ Modals: Proper z-index, overlay blocks
- ✅ Respects prefers-reduced-motion

## Performance
- **GPU Acceleration**: CSS Grid, Transforms
- **Image Optimization**: Lightweight sources (pravatar.cc, custom PNG)
- **Lazy Loading**: `loading="lazy"` on iframes
- **No Heavy JS**: Minimal DOM manipulation
- **Efficient Selectors**: Class-based CSS

## Testing Checklist
- [ ] All pages fit 100vh (except L5 center feed)
- [ ] Transitions smooth and continuous
- [ ] Modals centered and responsive
- [ ] Images load (including Ariel avatar)
- [ ] Buttons: hover, click, disabled states
- [ ] Flag validation works
- [ ] Level progression correct
- [ ] Mobile responsive (768px, 640px)
- [ ] No console errors
- [ ] Keyboard navigation works

## Future Enhancements
- Sound effects (level complete, transitions)
- Achievement badges
- Progress tracking / leaderboard
- Additional levels (6–10)
- Different social media themes (Instagram, Twitter, LinkedIn)
- Dark mode toggle
- Mobile native app
- Embedded video tutorials
- Difficulty levels (hints on/off)
- Certificate of completion
