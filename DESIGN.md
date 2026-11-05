---
name: Friendship Island Scoreboard
description: A hand-painted lifeguard-tower tournament board, projected live, with a quiet sand-paper control desk behind it.
colors:
  lifeguard-red: "#d42a2a"
  lifeguard-red-deep: "#9e1c1f"
  flag-yellow: "#f6c324"
  flag-yellow-deep: "#c9971a"
  card-cream: "#fbf3df"
  weathered-plank: "#f4ead2"
  bare-wood: "#d6bd8f"
  tar-ink: "#2b1d14"
  driftwood-ink: "#5a4434"
  ocean-teal: "#17a3b5"
  ocean-teal-deep: "#0f7f95"
  shallow-sky: "#a8e6ec"
  sand: "#ead09c"
  sand-deep: "#d8b77a"
  chalkboard-slate: "#26332d"
  chalk-white: "#f7f4ea"
  brass: "#c79a3e"
  rope: "#b88b52"
  desk-sand: "#efe1c0"
  desk-stroke: "#cdb88f"
  paper-white: "#ffffff"
  plum: "#6d1f5c"
  flamingo-pink: "#c85a8a"
  flamingo-blush: "#f8bfd5"
  lobster-red: "#bc1c34"
  lobster-blush: "#f6a9ab"
  dolphin-blue: "#1a8ae2"
  dolphin-sky: "#9fd5f7"
  seal-slate: "#6a84aa"
  seal-mist: "#bfd0ee"
  badge-white: "#fffdf3"
  name-cream: "#fffdef"
typography:
  numeral:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "196px"
    fontWeight: 700
    lineHeight: 1
    fontFeature: "tnum"
  display:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "88px"
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: "0.01em"
  team-name:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1
  title:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.01em"
  chalk:
    fontFamily: "'Josefin Sans', 'Century Gothic', sans-serif"
    fontSize: "40px"
    fontWeight: 700
    lineHeight: 1
  body:
    fontFamily: "'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: "15px"
    fontWeight: 650
    lineHeight: 1.45
  label:
    fontFamily: "'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: "13px"
    fontWeight: 650
    letterSpacing: "0.06em"
rounded:
  hardware: "4px"
  panel: "6px"
  plank: "8px"
  card: "10px"
  box: "12px"
spacing:
  hairline: "8px"
  row: "12px"
  card-gap: "16px"
  desk: "20px"
  board-gutter: "36px"
components:
  number-card:
    backgroundColor: "{colors.card-cream}"
    textColor: "{colors.tar-ink}"
    typography: "{typography.numeral}"
    rounded: "{rounded.card}"
    width: "156px"
    height: "236px"
  clock-card:
    backgroundColor: "{colors.card-cream}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.card}"
    width: "250px"
    height: "370px"
  header-sign:
    backgroundColor: "{colors.lifeguard-red}"
    textColor: "{colors.card-cream}"
    typography: "{typography.display}"
    rounded: "{rounded.plank}"
    height: "206px"
  team-card:
    backgroundColor: "{colors.weathered-plank}"
    rounded: "{rounded.card}"
    padding: "20px"
    width: "880px"
    height: "410px"
  team-badge:
    backgroundColor: "{colors.badge-white}"
    textColor: "{colors.paper-white}"
    typography: "{typography.team-name}"
    rounded: "{rounded.panel}"
    height: "300px"
  lead-tag:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.paper-white}"
    typography: "{typography.chalk}"
    padding: "6px 10px 3px"
  score-panel:
    backgroundColor: "{colors.flag-yellow}"
    rounded: "{rounded.panel}"
    height: "290px"
  chalk-slate:
    backgroundColor: "{colors.chalkboard-slate}"
    textColor: "{colors.chalk-white}"
    typography: "{typography.chalk}"
    rounded: "{rounded.panel}"
    padding: "6px 22px 8px"
  time-placard:
    backgroundColor: "{colors.flag-yellow}"
    textColor: "{colors.lifeguard-red}"
    rounded: "{rounded.box}"
    width: "880px"
    height: "400px"
  desk-box:
    backgroundColor: "{colors.card-cream}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.box}"
    padding: "18px 20px"
  button:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.tar-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.plank}"
    padding: "9px 14px"
  button-primary:
    backgroundColor: "{colors.lifeguard-red}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.plank}"
    padding: "9px 14px"
  button-gold:
    backgroundColor: "{colors.flag-yellow}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.plank}"
    padding: "9px 14px"
  button-danger-armed:
    backgroundColor: "{colors.tar-ink}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.plank}"
    padding: "9px 14px"
  score-input:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.tar-ink}"
    rounded: "{rounded.card}"
    padding: "4px 6px"
    width: "96px"
---

# Design System: Friendship Island Scoreboard

## Overview

**Creative North Star: "The Lifeguard Tower Board"**

The projected scoreboard is a physical object set on a beach of sky, ocean teal and sand: a short sun-faded red name sign at the top and four pale weathered team cards, each a plank board bolted together from a striped team badge and a yellow score panel. Every score and every timer digit is a cream wooden number card hanging from two brass hooks. Nothing glows, nothing is glass. Depth comes from paint over wood, soft cast shadows, brass bolts and rope, and the weight of cards that fall and swing. The board floats as a small pop-out beside the Canva slides, so it carries only the show name, scores and timer.

The board speaks the show deck's language. Lettering is the deck's Josefin Sans, the show name carries the deck's plum drop shade, and each team keeps the identity it has in the deck: its own color, its pale stripe color and its animal, set on a striped badge with the team name on a plate painted in the team color. The deck's Candice script was dropped from the board (2026-11-04) because it did not read at pop-out size.

The board is composed once at a fixed 1920x1080 stage and scaled uniformly to the screen, so the room always sees the same picture. Density is low and type is huge: numerals are the content, everything else is hardware that holds them up. Texture is generated, not photographed: an `feTurbulence` wood grain multiplied over the paint and the team badges, bare-wood flakes masked to plank edges, plank seams, sand grain over the beach and a sun-fade on the red header.

The operator's control window is the same world at desk scale: sand-paper ground, cream boxes, Josefin Sans for headings and the large score readouts, team adjectives in their team colors, and a plain system UI face for everything the operator reads under pressure. It borrows the palette and the display face, not the wood.

**Key Characteristics:**
- Painted wood, rope and brass; no gradients-as-glow, no glass, no neon.
- One bold geometric face (Josefin Sans 700) for everything the audience reads, team names included.
- Each team carries its deck identity: team color, stripe color, name plate, animal art.
- Fixed digit slots: a number never reflows, a card swaps in place.
- Change is a physical event: cards fall off hooks, new cards drop on with weight and swing.
- Fixed 16:9 stage scaled to fit and clipped to its frame, never reflowed.

## Colors

Sun-faded lifeguard paint (red and flag yellow) over pale weathered plank, with a teal and sand beach behind, near-black brown ink on cream, a deck plum accent, and four team identity pairs taken from the deck.

### Primary
- **Lifeguard Red** (lifeguard-red): the header sign paint, the leader flag's top half, the TIME! lettering and red inner border, the timer numerals at time's up, the control view's app title, its "in the lead" note and its primary action. The board's loudest voice.
- **Deep Lifeguard Red** (lifeguard-red-deep): the painted drop shade under the TIME! lettering; the pressed edge of the primary button.

### Secondary
- **Flag Yellow** (flag-yellow): the score panel each pair of number cards hangs on, the TIME! placard, the leader flag's lower half, the timer nails, and the gold preset buttons (timer lengths, placement bonuses) in the control view.
- **Deep Flag Yellow** (flag-yellow-deep): stroke and pressed edge for gold buttons; shade on nail heads.

### Tertiary
- **Deck Plum** (plum): the deck-style drop shade under the show name, and the "in the lead" note in the control view.
- **Ocean Teal** (ocean-teal) and **Deep Ocean Teal** (ocean-teal-deep): the sea band behind the board. Deep teal is also the focus ring and the pressed "Board shows" button in the control view, the only interactive use of the sea.
- **Shallow Sky** (shallow-sky): the sky above the sea band.

### Team Identity
Each team has an outline color and a light stripe color, sampled from the deck's team slides.
- **Flamingo Pink / Flamingo Blush** (flamingo-pink, flamingo-blush): Fierce Flamingos.
- **Lobster Red / Lobster Blush** (lobster-red, lobster-blush): Lucky Lobsters.
- **Dolphin Blue / Dolphin Sky** (dolphin-blue, dolphin-sky): Daring Dolphins.
- **Seal Slate / Seal Mist** (seal-slate, seal-mist): Snazzy Seals.

The team color paints the name plate under the team name on the board and colors the team's adjective in the control view. The light color alternates with Badge White (badge-white) in the badge's diagonal stripes. Team names are Paper White on the plate.

### Neutral
- **Card Cream** (card-cream): number cards, lettering on the red sign, control-view boxes.
- **Weathered Plank** (weathered-plank): team cards, the default `.wood` paint.
- **Bare Wood** (bare-wood): exposed wood showing through chipped paint.
- **Tar Ink** (tar-ink): numerals, the team noun in the control view, all body text.
- **Driftwood Ink** (driftwood-ink): secondary text in the control view (help copy, status, log, labels).
- **Sand / Deep Sand** (sand, sand-deep): the beach floor of the projector stage; page background.
- **Chalkboard Slate / Chalk White** (chalkboard-slate, chalk-white): the hanging "just scored" slate and the fullscreen hint.
- **Brass / Rope** (brass, rope): hooks, bolts, flag holder, rope hangers.
- **Desk Sand / Desk Stroke / Paper White** (desk-sand, desk-stroke, paper-white): the control view's ground, the stroke on neutral buttons and inputs, and button/input faces; paper white is also the lead tag's lettering.

### Named Rules
**The Paint Not Light Rule.** Color is paint on a surface. It is laid flat over wood grain and shaded by soft cast shadows; it never glows, blooms or gradients toward neon. The only gradients are physical: sky to sea to sand, a sun-fade on the red sign, the curve of a cream card, and the painted stripes of a team badge.

**The Two Flag Colors Rule.** Red and yellow are the lifeguard's signal colors and carry board state: red marks the header, the leader's flag and the TIME! moment; yellow holds the numbers. Team colors identify teams and never signal state.

**The Deck Identity Rule.** A team's two colors belong to that team alone, and they always travel with its name and animal. Color is never the only thing that tells two teams apart.

## Typography

**Display Font:** Josefin Sans (self-hosted variable woff2, weights 100-700, used at 700; falling back to Century Gothic, sans-serif)
**Team names:** Josefin Sans 700, the same face as everything else the audience reads.
**UI Font:** Segoe UI (system-ui stack), control view only

**Character:** A bold geometric sans carries numerals, the show name, team names, notes and control headings, matching the deck. The system UI face is reserved for operator chrome, where speed of reading beats character.

### Hierarchy
- **Numeral** (700, 196px on score cards, 320px on clock cards, 72px control readout, 44px score input; line-height 1, tabular figures): every score and time digit.
- **Display** (700, 88px, 0.98, 0.01em): the show name on the name sign, one line at 76px, cream with a plum drop shade; 230px for TIME!.
- **Team Name** (700, 48px, fitted down to 28px only if it would overflow the 400px plate; line-height 1): one line, adjective and noun, Paper White with a soft painted shade on the team-color plate.
- **Title** (700, 20-30px, 1): control-view headings; the 24px team name in each control row.
- **Chalk** (700, 40px slate, 26px lead tag and hint, 20px control lead note; line-height 1): transient notes. Same face as Display; the role marks what is fleeting.
- **Body** (650 for buttons at 15px; 400 at 14px/1.45 for help copy): control view.
- **Label** (650, 13px, 0.06em, uppercase): the inline field label before a control row ("Length").

### Named Rules
**The Back Row Rule.** If the audience reads it, it is set in Josefin Sans 700, except team names. System sans never appears on the projector.

**The Team Plate Rule.** A team's name always sits on its own color plate, under its animal; it never floats on the stripes.

**The Tabular Rule.** Every numeral that can change uses tabular figures in a fixed-width slot, so a 1 never shifts its neighbors.

## Layout

The projector view is a fixed 1920x1080 stage, centered and uniformly scaled with `min(innerWidth/1920, innerHeight/1080)`, with overflow hidden so nothing (such as the parked TIME! placard) draws outside the frame; the surround shows sky, sea and sand. The board is a small pop-out beside the Canva slides, so it carries only the show name, scores and timer. Composition from top: a short red name sign (128px tall, sized to the show name) centred at y 30; then the four team cards. No posts, braces or crossbeam: the cards move between views, so nothing pretends to hold them in place.

Two views share the stage. **Scores view:** four 880x410 team cards in a 2x2 grid under the name sign (columns at x 60 and 980, rows at y 196 and 636), reading Flamingos, Lobsters / Dolphins, Seals. **Timer view:** each card scales to 50% and slides straight out to its own side, two per side and stacked (left column x 30, right column x 1450, rows at y 380 and 615); the name plates fade out so only the animal and score remain; a yellow clock board (900x420) hangs from the name sign on two long ropes, centred at x 960, y 390, holding four 186x280 clock cards around two nails. The TIME! placard lands over the clock board at y 400.

Inside a team card (20px padding, 20px gap): the striped team badge (400x370) with animal art top-right, leader flag and lead tag top-left and the name plate (80px, team color) across its foot; then the yellow score panel (fills the rest, 370px tall) holding two 178x270 number cards 18px apart. The tens slot is always present; below 10 it shows a blank cream card.

The control view is a two-column grid (`minmax(420px,1fr) minmax(560px,1.25fr)`, 20px gap) of cream boxes on desk sand: preview and timer left, scores and change log right. It collapses to one column at 1100px; at 640px team rows restack, art shrinks to 48px and the score input moves inline. Controls sit in wrapping rows with 8px gaps and 12px between rows.

## Elevation & Depth

Depth is physical and layered: soft, warm-brown cast shadows lift objects off what they hang on, inset highlights and shadows give planks thickness, and texture (grain, flakes, seams) gives surfaces material. Shadows are always blurred, tinted brown-black, and fall downward; the only hard offsets are painted drop shades on sign lettering.

### Shadow Vocabulary
- **Team card** (`box-shadow: 0 18px 26px rgba(40,25,10,.38), inset 0 -8px 0 rgba(90,60,30,.12)`): team cards; the name sign uses `0 14px 24px rgba(60,20,10,.35)` plus inset top highlight and bottom shade.
- **Badge** (`box-shadow: inset 0 0 0 4px rgba(255,255,255,.55), inset 0 -6px 12px rgba(80,50,30,.12), 0 4px 8px rgba(60,40,10,.18)`): team badges, a pale painted rim set into the plank.
- **Hanging card** (`box-shadow: 0 12px 14px rgba(40,25,10,.35), inset 0 0 0 3px rgba(120,90,50,.18)`): number cards.
- **Placard** (`box-shadow: 0 30px 50px rgba(30,15,5,.5), inset 0 0 0 10px #d42a2a`): the TIME! placard, the highest object on the board.
- **Bolt** (`box-shadow: 0 2px 3px rgba(0,0,0,.35)`): brass bolts.
- **Painted drop shade** (`text-shadow: 4px 5px 0` plus a soft `5px 8px 10px rgba(0,0,0,.25)` under the show name): plum under the show name; deep red under "Team Scores"; TIME! uses `6px 8px 0` deep red.
- **Plate shade** (`text-shadow: 3px 4px 0 rgba(0,0,0,.22)`): team names on their color plate, a painted shade on a painted surface.
- **Desk box** (`box-shadow: 0 1px 3px rgba(90,60,30,.18), 0 10px 22px rgba(90,60,30,.16)`): control-view boxes.

### Named Rules
**The Gravity Rule.** Every shadow falls down and warm. Nothing floats on a neutral gray blur.

**The Sign-Painter Shade Rule.** A hard offset shade belongs only to painted lettering on a painted sign, in plum (the show name) or the sign's own deep tone. It never sits under a box, card or button.

## Shapes

Lightly eased rectangles throughout: hardware 4px, panels and badges 6px, planks and buttons 8px, number cards 10px, boxes and the placard 12px; the lead tag is a 5px-radius slip set at -4 degrees. Circles are reserved for hardware (bolts, nails, the status dot). Team badges clip their 135-degree stripes and art to their own edge. Recurring silhouettes are physical fixtures: two brass hooks over every number card with two punched holes, two ropes over every plank, bolts in plank corners.

## Components

### Number Card (signature)
Cream card with a top-to-bottom curve (`#fffaf0` to card cream to `#f1e5c8`), two punched holes, hung from two brass hooks in a fixed slot (156x236 on scores, 250x370 on the clock). On a score change the old card falls off (0.48s, accelerating, rotates 9 degrees, fades) while the new card drops from above and swings to rest (0.95s, overshoot then damped rotation 3.5 to -2 to 0.8 degrees), followed by a one-beat dashed chalk outline that fades over 1.6s. Clock digits use a lighter flick (0.22s out, 0.28s drop in) so the timer ticks without spectacle.

### Team Badge (signature)
The team's deck identity set into its card: 135-degree diagonal stripes, 24px each, alternating the team's light color and badge white, under a grain multiply at 0.35 and a pale 4px inner rim. The team emblem is centred above the name plate (272px tall, soft drop shadow) and, once the plate fades in the timer view, recentres in the whole badge at 108%. Each emblem is the deck animal with its deck prop, composed by tools/compose_art.py from the deck sources: flamingo with the angry mark, lobster with the coin pile, dolphin with the beach ball, seal with its pixel sunglasses (always shown) and sparkles. The name plate runs across the foot.

### Team Card
Weathered plank with one vertical seam and a bolt in each corner. Holds the team badge and the yellow score panel side by side. In the view change it moves as one piece (0.75s, exponential ease-out); the plate fades out (0.35s) on the way to the timer view and back in after the card has landed. The leader flies a red/yellow lifeguard flag (94x62 on a 184px pole in a brass holder) in the top-left corner of its own badge; as it rises, the emblem steps 58px right and down to 84% so the two never overlap, and steps back when the lead is lost. The flag rises (0.55s), unfurls (0.35s after 0.45s) and flutters once (1.1s), then hangs still; losing the lead furls the flag (0.3s) and then drops the pole (0.5s). The board has no "in the lead" text tag; the control view still names the leader. Ties raise every tied flag.

### Header Sign
Red painted plank with a horizontal seam, sun-fade, extra grain multiply and edge-chipped paint. Short, centred, sized to the one-line show name, with a bolt in each corner. It holds nothing else.

### Clock Board and View Change
Yellow painted plank (the Two Flag Colors Rule: yellow holds numbers) hung from the name sign on two ropes, holding the four clock cards. Switching to the timer view: the team board shrinks and drops (0.75s, exponential ease-out), and the clock board drops in from above the stage and swings to rest (1.25s, damped rotation 1.6 to -0.9 to 0.35 degrees). Switching back: the clock board hoists up out of frame (0.42s, accelerating), then the team board grows back into place (0.75s after 0.28s).

### Chalk Slate
Small slate pinned over the top edge of the score panel, Josefin Sans text such as "+10 · 1st place". It swings in on change (1.4s damped) and fades after 6 seconds.

### TIME! Placard
Yellow plank with a 10px red inner border and red lettering, hung on long ropes. At zero it drops in from above the stage (1.3s with swing), the board shudders (0.6s), the header flashes yellow/red six times, and the clock numerals turn red.

### Buttons (control view)
- **Shape:** gently eased (8px).
- **Default:** paper white, tar ink, 650 weight, `inset 0 0 0 2px` desk-stroke rim with a 3px bottom lip; hover warms to `#fff8e6`; active presses down 2px and drops the lip.
- **Primary:** lifeguard red with white text and a deep-red lip; one or two per view (Pop out over slides, Start/Pause).
- **Gold:** flag yellow with deep-yellow rim; timer presets and placement bonuses.
- **Danger:** looks default at rest; first click arms it to tar ink with "Click again to reset" for 3.5s.
- **Focus:** 3px deep-teal outline, 2px offset. Icons are inline 16px stroke SVG.

### Inputs (control view)
Paper white with a 2px desk-stroke border, tabular figures, centered. The per-team score input is set in Josefin Sans 700 at 44px. The "Board shows" toggle is two joined buttons (Scores, Timer); the shown view is pressed in deep teal with white text.

### Desk Box
Cream box, 12px radius, 18px 20px padding, desk-box shadow, Josefin Sans heading. Team rows inside are divided by a 2px dashed sand line; each row names the team with its adjective in the team's outline color and its noun in tar ink.

## Do's and Don'ts

### Do:
- **Do** put every changing number on a cream card in a fixed hooked slot, with tabular Josefin Sans numerals.
- **Do** make changes physical: fall, drop with weight, swing to rest, then a single chalk afterglow.
- **Do** build surfaces as paint over generated wood grain, with bare wood showing only at plank edges.
- **Do** hang things: rope, hooks, bolts and wires explain why every object is where it is.
- **Do** give each team its deck identity together: team color plate, stripe color, name and animal art.
- **Do** keep red and yellow for board state, and team colors for team identity.
- **Do** honor `prefers-reduced-motion`: all animation and transition off, the placard simply present at time's up.
- **Do** keep the control view in the palette and Josefin Sans, with system UI text for operator reading.

### Don't:
- **Don't** use glossy game-show panels, glowing gradients, glass or neon.
- **Don't** let a number reflow its neighbors or change width as it updates.
- **Don't** set audience-facing text in the system sans.
- **Don't** put hard offset shadows under boxes, cards or buttons; that shade belongs to painted lettering only.
- **Don't** set a team name straight on the striped badge; it goes on its color plate.
- **Don't** use a team's colors for another team, for board state, or as the only way to tell teams apart.
