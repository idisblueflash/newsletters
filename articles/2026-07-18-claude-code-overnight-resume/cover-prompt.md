# Cover Image Prompt

场景：猫头鹰守夜（安全感）— 人已熟睡，猫头鹰在窗台转头望向书桌，月光连接两者，窗外可见月色下的屋顶与树影，右扇窗微开。

## Base prompt (text-to-image, generated with composition.png as object-arrangement guide)

```
Generate a cinematic storyboard panel in dramatic ink illustration style —
extreme high-contrast black and white, bold brushstrokes, woodcut-like
rendering, the visual language of professional film pre-visualization.

The attached image is an abstract compositional guide for OBJECT ARRANGEMENT
ONLY: gray shapes mark where solid objects/dark masses should be placed,
white marks negative space, and the converging diagonal lines mark the focal
point where key elements should meet. Do NOT render any grid lines, triangles,
or diagram artwork into the final output — the final image must be a clean
finished ink illustration with zero visible guide lines or overlays.

Map the guide's zones to these objects:
- The solid gray rectangular block in the upper-left (roughly the left third,
  upper two-thirds of frame) = the window with the owl on its sill.
- The wedge/triangle converging near the center of the frame = the writing
  desk with the glowing laptop, positioned at the wedge, with the moonlight
  shaft converging there too.
- The gray band spanning the ENTIRE width along the bottom third, rising up
  the right edge = the bed and blanket, spanning from the left edge all the
  way to the right edge, with the headboard/pillow area raised higher on the
  right edge.

— LAYER 1: Concrete Nouns —
Camera positioned at a gentle elevated angle from a corner near the ceiling,
a soft three-quarter high view — not a direct overhead shot — framing the
whole bedroom without feeling like surveillance.

An owl perches on a wooden windowsill inside the upper-left gray zone,
occupying no more than 4% of the frame — noticeably small against the window
opening. Its head is turned mid-rotation toward the desk across the room,
feathers slightly fluffed, one eye wide open catching a sliver of moonlight,
talons gripping the sill motionless. No candle or candlestick on the
windowsill.

Through the window glass, a nocturnal outdoor scene is visible beyond the
owl: distant rooftops and bare treetops under a pale moonlit sky, faint and
slightly hazy, rendered in the same high-contrast ink style — the outside
world reads as a soft backdrop, not competing with the owl.

In the bed spanning the full bottom of the frame, a human figure lies asleep
under a blanket, rendered as a soft curled silhouette, facing away from the
camera, tucked into the right-rising portion of the bed mass.

At the central wedge, a writing desk sits in the middle distance. A laptop
screen glows faintly on it, reduced to a dim rectangle of soft light in the
background, no readable text or letterforms.

Curtains frame the window unevenly — one drawn back further than the other.
A wardrobe and its shadow intrude from the left edge of the frame,
asymmetrically, not mirrored on the right.

Moonlight streams through the window in a single soft diagonal shaft,
converging near the center of the frame at roughly mid-height where the desk
sits, visually bridging the owl and the sleeping figure. Everything outside
this shaft sinks into deep ink-black shadow.

— LAYER 2: Visual Anchor Words —
Two subjects at different states, one perched and alert / one curled and
still, connected by a single soft beam of light crossing the negative space
between them. Negative space cushions both subjects rather than isolating
either one. Quiet vigil — the alert subject faces the sleeping one, not the
camera.

Render in dramatic ink storyboard style: extreme black and white ink contrast,
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines,
woodcut-like rendering. No soft shading. No color. No text, no letters, no
handwriting, no annotations, no captions, no grid lines, no diagram overlays
anywhere in the image.

— LAYER 3: Magic Words —
ultra-detailed, cinematic lighting, woodcut print quality, film grain

Aspect ratio: 21:9 ultra-wide cinematic panel.
```

Input image for this generation: `cover/composition.png` (object-arrangement guide, not rendered).

## Variant: camera follows the owl outside (fully exterior scene)

场景改动：完全放弃室内构图（不再有卧室、床、书桌、衣柜）。镜头跟着猫头鹰到了室外，主体是树干上的猫头鹰，背景是外面的夜色屋顶。只保留上一版里"窗外那个场景"的元素——月色下的屋顶、光秃的树枝、朦胧的天空——把它从背景升格为整个画面的主场景。

```
Generate a cinematic storyboard panel in dramatic ink illustration style —
extreme high-contrast black and white, bold brushstrokes, woodcut-like
rendering, the visual language of professional film pre-visualization.

— LAYER 1: Concrete Nouns —
Camera positioned at a low, slightly upward angle from ground level, looking
up along the trunk of an old gnarled tree — an exterior night shot, no
interior room, no window frame, no glass.

An owl perches on a thick bare branch jutting from the trunk, positioned at
the upper-left rule-of-thirds intersection, occupying no more than 6% of the
frame. Feathers slightly fluffed against the cold air, one eye wide open
catching a sliver of moonlight, talons gripping the rough bark motionless,
head turned mid-rotation as if listening to something in the distance.

The tree's trunk and branches intrude asymmetrically from the lower-left
edge of the frame, bark texture rendered in bold ink linework, cracks and
knots visible. Bare twigs fork off unevenly into the upper frame, breaking
the silhouette of the sky.

Beyond the tree, a row of distant rooftops and chimneys recedes into the
night, small and hazy, occupying the lower-right third of the frame. Among
them, one single small window glows faintly with warm light — the only
warm-toned or brightly lit rectangle in an otherwise cold, dark scene — a
quiet, distant trace of the bedroom left behind, no figure visible in it.

A pale, near-full moon hangs in the upper-right area of the frame, partially
veiled by thin drifting clouds, casting the only strong light source in the
sky.

Moonlight rakes diagonally across the tree bark and the owl's feathers,
throwing a hard-edged shadow of the branch across the rooftops below.
Everything outside this raking light sinks into deep ink-black shadow.

— LAYER 2: Visual Anchor Words —
A solitary sentinel on a branch, facing away from the camera toward the
distant lit window, vast negative sky pressing down from above, the single
warm window a small anchor of memory in a cold exterior. Quiet vigil rather
than threat — stillness held against open night air.

Render in dramatic ink storyboard style: extreme black and white ink contrast,
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines,
woodcut-like rendering. No soft shading. No color. No text, no letters, no
handwriting, no annotations, no captions anywhere in the image.

— LAYER 3: Magic Words —
ultra-detailed, cinematic lighting, woodcut print quality, film grain

Aspect ratio: 21:9 ultra-wide cinematic panel.
```

This variant is text-to-image (no composition.png reference — the object layout is fully new).

## Edit chain (image-to-image, applied in order on top of the base render)

1. **Linework refinement** (preview → medium):
   ```
   Keep the composition, characters, and lighting identical. Just refine linework quality.
   ```

2. **Window half-open** (first attempt, direction was wrong — kept for record):
   ```
   Keep everything else in this image completely identical — same composition,
   same owl, same bed, same desk, same lighting, same style. The only change:
   the window should be shown half-open — one of the two window panels
   tilted/ajar open into the room, as if letting in the night air, while the
   other panel stays closed. Keep the owl perched on the sill exactly as is.
   ```

3. **Fix window direction** — left panel closed, right panel opens inward:
   ```
   Keep everything else in this image completely identical — same composition,
   same owl, same bed, same desk, same lighting, same style, same curtains.
   Fix only the window: the LEFT window panel (the one nearest the owl) must
   be fully closed and flat against the frame, flush with the glass. The
   RIGHT window panel must be the one that is open, swung inward into the
   room on its hinge, tilted at an angle so its glass and handle are visible
   catching the light. The owl stays perched on the sill exactly as before,
   near the closed left panel.
   ```

4. **Reduce opening angle to ~30°** (previous attempt over-corrected to a
   separate door-like element — the fix explicitly pins it to the single
   existing window):
   ```
   Keep everything else in this image completely identical — same composition,
   same owl, same bed, same desk, same lighting, same style, same curtains.
   There is exactly ONE window in this room, located in the upper-left area
   where the owl perches on its sill. Do not add any second window or door
   elsewhere in the room. On this single window: the left panel (nearest the
   owl) stays fully closed and flush. The right panel of this SAME window
   should be barely ajar, opened only about 30 degrees from flush — just a
   subtle crack, not swung wide open. Keep the handle and hinge in the same
   place as before.
   ```

5. **Open right panel a bit wider (~45°)** — final state used in `cover.png`:
   ```
   Keep everything else in this image completely identical — same composition,
   same owl, same bed, same desk, same lighting, same style, same curtains,
   same closed left window panel. There is exactly ONE window, the one where
   the owl perches. Adjust only the right panel's opening angle: open it a
   bit wider than its current subtle crack — roughly 45 degrees from flush,
   noticeably more open but still not swung all the way out. Keep the handle
   and hinge in the same place.
   ```

Output: `cover/cover.png`

## Variant: owl on a tree trunk outside the window

场景改动：猫头鹰不再站在室内窗台上，而是站在窗外一棵老树的树干/枝杈上，隔着玻璃被看见。室内窗台空出来，月光和构图其余部分不变。

```
Generate a cinematic storyboard panel in dramatic ink illustration style —
extreme high-contrast black and white, bold brushstrokes, woodcut-like
rendering, the visual language of professional film pre-visualization.

The attached image is an abstract compositional guide for OBJECT ARRANGEMENT
ONLY: gray shapes mark where solid objects/dark masses should be placed,
white marks negative space, and the converging diagonal lines mark the focal
point where key elements should meet. Do NOT render any grid lines, triangles,
or diagram artwork into the final output — the final image must be a clean
finished ink illustration with zero visible guide lines or overlays.

Map the guide's zones to these objects:
- The solid gray rectangular block in the upper-left (roughly the left third,
  upper two-thirds of frame) = the window, seen from inside the bedroom.
- The wedge/triangle converging near the center of the frame = the writing
  desk with the glowing laptop, positioned at the wedge, with the moonlight
  shaft converging there too.
- The gray band spanning the ENTIRE width along the bottom third, rising up
  the right edge = the bed and blanket, spanning from the left edge all the
  way to the right edge, with the headboard/pillow area raised higher on the
  right edge.

— LAYER 1: Concrete Nouns —
Camera positioned at a gentle elevated angle from a corner near the ceiling,
a soft three-quarter high view — not a direct overhead shot — framing the
whole bedroom without feeling like surveillance.

The window sits inside the upper-left gray zone, its sill empty. Through the
window glass, an old gnarled tree stands just outside, its trunk and a bare
branch crossing close to the glass. An owl perches on that tree trunk/branch
outside the window, positioned at the upper-left rule-of-thirds intersection
as seen through the glass, occupying no more than 4% of the frame — small
and partially veiled by the glass and window frame. Its head is turned
mid-rotation toward the desk across the room, feathers slightly fluffed, one
eye wide open catching a sliver of moonlight, talons gripping the bark
motionless. No candle or candlestick anywhere on the windowsill.

Beyond the tree, a nocturnal outdoor scene recedes into the distance: faint
rooftops under a pale moonlit sky, hazy and soft, rendered in the same
high-contrast ink style — the outside world reads as a soft backdrop, not
competing with the owl or the tree.

In the bed spanning the full bottom of the frame, a human figure lies asleep
under a blanket, rendered as a soft curled silhouette, facing away from the
camera, tucked into the right-rising portion of the bed mass.

At the central wedge, a writing desk sits in the middle distance. A laptop
screen glows faintly on it, reduced to a dim rectangle of soft light in the
background, no readable text or letterforms.

Curtains frame the window unevenly, drawn back to each side, not obscuring
the tree or the owl. A wardrobe and its shadow intrude from the left edge of
the frame, asymmetrically, not mirrored on the right.

Moonlight streams through the window and past the tree branch in a single
soft diagonal shaft, converging near the center of the frame at roughly
mid-height where the desk sits, visually bridging the owl outside and the
sleeping figure inside. Everything outside this shaft sinks into deep
ink-black shadow.

— LAYER 2: Visual Anchor Words —
Two subjects at different states, one perched and alert outside the glass /
one curled and still inside, connected by a single soft beam of light
crossing the negative space between them, a pane of glass separating without
isolating. Negative space cushions both subjects rather than isolating
either one. Quiet vigil — the alert subject faces the sleeping one, not the
camera.

Render in dramatic ink storyboard style: extreme black and white ink contrast,
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines,
woodcut-like rendering. No soft shading. No color. No text, no letters, no
handwriting, no annotations, no captions, no grid lines, no diagram overlays
anywhere in the image.

— LAYER 3: Magic Words —
ultra-detailed, cinematic lighting, woodcut print quality, film grain

Aspect ratio: 21:9 ultra-wide cinematic panel.
```

Input image for this generation: `cover/composition.png` (object-arrangement guide, not rendered).
