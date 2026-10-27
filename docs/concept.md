# Concept v0.1
Historical comparison baseline. The selected direction and current room requirements are in [slim v0.2](slim-v02.md).

Preliminary engineering proposal, 2026-10-27. All dimensions below are millimeters unless marked otherwise. Do not cut extrusion from this document until actual filters, joints and fan mounting geometry are confirmed.

## Design objectives

- Quiet continuous use: target 200 CFM particle CADR at ≤35 dBA at 1 m; 30 dBA is a stretch goal.

- Provisional room: 300 ft² × 8 ft = 2,400 ft³. Required CADR = volume × desired clean-air changes/hour ÷ 60 = 200 CFM for 5/hour.

- Easy servicing: filters removable without taking apart the frame or fan wiring.

- Simple fabrication: straight extrusion cuts, flat panels and small printed parts.

- Appearance: natural or black extrusion, matte printed corner caps, matching side panels, exposed white filter faces or removable open guards. Optional wood veneer goes on sealed narrow sides.

- Provisional incremental budget: about $200–355 excluding existing extrusion, tools, shipping, tax and test instruments. This is a planning allowance, not vendor pricing.

## Air path and layout

Room air enters through two opposing broad filter faces, passes into a common clean-air plenum, and exits upward through a 3 × 2 fan array. The bottom and narrow sides are airtight. Both filter arrows point inward. All fans exhaust from the plenum.

Use nominal 20 × 20 × 1 inch MERV 13 filters as the first candidate. Filtrete MPR 1900 is a research-backed reference product, but exact SKU, actual dimensions, local availability and pressure drop remain procurement checks.

Illustrative frame envelope is **550 W × 360 D × 550 H** (about 21.7 × 14.2 × 21.7 inches), excluding feet, external panels, guards and retainers. This assumes an illustrative 508 × 508 filter and 1 mm clearance per edge; nominal filter labels often differ from actual dimensions.

Let:

- Fw, Fh, Ft = measured filter frame width, height, thickness;

- c = fit clearance per edge, initially 1 mm;

- e = extrusion width, 20 mm.

Then W = Fw + 2c + 2e; H = Fh + 2c + 2e. Keep D = 360 initially. Aperture width and height are W − 40 and H − 40. Printed shoulder rails sit behind the cardboard perimeter and carry continuous closed-cell gaskets. Design their overlap from the actual cardboard rim so the media is not crushed or unnecessarily masked. Retainers press the filter onto those gaskets; loose slide channels alone are not airtight.

A continuous gasket on every panel and filter seat matters: the plenum operates below room pressure, so cracks admit unfiltered air.

## Frame and panels

Use four full-height vertical posts, four width rails between posts, and four depth rails between posts. Top and bottom rails occupy the top/bottom 20 mm of the post height. Width rails occupy front/back planes; depth rails run between them along the sides.

| Part | Qty | Formula | Illustrative length |
| --- | ---: | --- | ---: |
| Vertical 2020 posts | 4 | H | 550 |
| Front/back horizontal rails | 4 | W − 40 | 510 |
| Side horizontal rails | 4 | D − 40 | 320 |

Net extrusion length is 5.52 m before kerf and stock planning. Joint brackets must fit without colliding with filter seats; confirm the actual slot width, T-nut size and bracket footprint. Use metal structural brackets, with printed parts for seals, retention and trim.

Top and bottom sheet panels cover the 550 × 360 frame. Two narrow side panels close the ends; their exact cuts depend on surface versus inset mounting. Start with approximately 6 mm plywood panels, sealed and fully cured. A removable top plate supports the six fans below it, leaving their exhaust guards above. Inspect plate stiffness and add support if needed.

Illustrative fan centers in top view, measured from one outer corner:

- X = 125, 275, 425

- Y = 105, 255

Six 140 mm square fan bodies fit inside the 510 × 320 clear top opening with 10 mm between bodies. Confirm corner brackets, wiring, screws and guards do not intrude. Fan cutouts and screw patterns must come from the actual fan drawing; the concept SVG is not a drilling template.

## Fan control and wiring

Candidate: six identical ARCTIC P14 PWM PST 12 V fans. Start with one sample to assess tonal noise before buying the full set. Compare at useful airflow, not only idle sound.

Use a standalone four-wire PC-fan PWM controller and adequately rated distribution harness. Supply constant 12 V to the fans and a compatible PWM control signal; a generic two-wire LED dimmer is not equivalent. Share ground, use only one tach signal per controller input, and verify startup at the lowest selected setting.

The reference fan rating gives 6 × 0.12 A = 0.72 A nominal, or 8.64 W for fans alone. A reputable safety-listed external 12 V, 2 A supply is a candidate, subject to startup and controller-load checks. Verify connector polarity and harness current ratings. Add strain relief and a fuse selected to protect the actual wire and connectors while accommodating startup. Keep mains wiring inside the external supply.

Provide guards wherever blades are accessible, including during foreseeable filter servicing. Isolate vibration with gaskets/washers, retain fans mechanically, and keep leads clear of blades. Do not mount a dense decorative mesh directly against the fan blades.

## Printed parts

Model these after measuring the real components:

1. Filter shoulder/gasket rail segments, joined with sealed overlaps.
2. Captive screw or quarter-turn filter retainers; screws are the simplest first prototype.
3. Rounded corner caps and extrusion end caps.
4. Cable clips and strain-relief mount.
5. Rubber-foot adapters if necessary.

PETG is a reasonable initial material for trim and clips. Use a small fit coupon to confirm slot and fastener fits. Keep each part within the actual printer bed. Do not rely on printed clips for the primary structural joints or carrying loads.

## Preliminary bill of materials

| Item | Quantity | Allowance, USD |
| --- | ---: | ---: |
| 2020 extrusion | 5.52 m net, illustrative | Existing stock |
| MERV 13 filters | 2 | 40–65 |
| 140 mm PWM fans | 6 | 45–80 |
| External 12 V supply, controller, harness, fuse and strain relief | 1 set | 35–60 |
| Metal brackets, matching T-nuts and screws | 1 set | 25–45 |
| Top/bottom/side sheet material and finish | 1 set | 20–40 |
| Fan guards, foam seals, isolation and feet | 1 set | 25–45 |
| Printed retainers/trim | 1 set | 10–20 |
| **Total excluding existing stock and tools** | | **200–355** |

These estimates are not shopping quotes. Premium fans, cosmetic screens, extra extrusion and measuring equipment can raise the total.

## Build sequence

1. Confirm room, space and acoustic target. Obtain sample filter and fan; measure them.
2. Make a taped temporary two-filter plenum with the intended fan array and guards. Sweep fan speed to test whether the concept has enough performance headroom.
3. Finalize frame parameters, bracket clearance and a printed gasket-seat fit coupon.
4. Cut/deburr extrusion and square the frame using metal brackets.
5. Fit and seal bottom/side panels; install continuous filter seats and gaskets.
6. Cut the top plate using confirmed fan drawings; fit fans, guards and removable wiring.
7. Install filters and retainers, then check for bypass leaks, rattles and secure retention.
8. Measure the complete cabinet at several speeds before adding cosmetic screens. Recheck after screens are added.
9. Mark useful normal and sleep settings with their measured cleaning performance.

## CAD handoff

Fusion 360 is appropriate after filter measurements and frame details are fixed. Use named parameters for Fw/Fh/Ft, clearance, extrusion width, cabinet depth, panel thickness, gasket compression and fan pitch. Model separate components for frame, panels, filter envelopes, fans and each printed fitting. Export editable F3D plus STEP for the assembly, STL/3MF for printed parts and DXF/PDF for flat panels.

The current drawing is an original layout study, not a detailed Fusion model. It intentionally leaves production holes, joint hardware and retention geometry unresolved.
