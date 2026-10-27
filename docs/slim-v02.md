# Slim cabinet v0.2

Selected development direction, 2026-10-27. The user has a Bambu H2D and approximately 600 ft² of open living space connected to upstairs and downstairs hallways. Multiple units are acceptable. Ceiling height, connected volume, budget ceiling, extrusion profile and exact filters remain unknown.

## System plan: prototype one, then size the fleet

Develop one repeatable slim unit targeting 200 CFM particle CADR at no more than 35 dBA at 1 m. Both values must be achieved at the same setting; neither has been measured. Build and measure the first prototype before duplicating it.

For 600 ft² alone:

| Ceiling height | Volume | CADR for 5 clean-air changes/hour |
| --- | ---: | ---: |
| 8 ft | 4,800 ft³ | 400 CFM |
| 9 ft | 5,400 ft³ | 450 CFM |
| 10 ft | 6,000 ft³ | 500 CFM |

Each additional 1,000 ft³ of connected space adds about 83 CFM to that design target. At 8 ft ceilings, each extra 100 ft² adds about 67 CFM. Include stairwell volume once; avoid double-counting it as both upstairs and downstairs area.

Two units delivering a measured 200 CFM each would nominally provide 5 equivalent clean-air changes/hour in the 600 ft², 8 ft-high space alone. Three would provide 600 CFM combined, equivalent to 7,200 ft³ at 5/hour. These are well-mixed volume calculations, not a promise of equal cleaning throughout connected floors. Hallway and stairwell air exchange is uncertain.

Place two units apart within the occupied open-plan area, with both filter faces and side outlets unobstructed. Prioritize a separate unit on another occupied floor over assuming one downstairs unit cleans upstairs effectively. Use a 150 mm clearance around intakes and 300 mm at side outlets as initial prototype placement allowances, then assess drafts and mixing; these are not tested minimums. Do not put either filter face flat against a wall.

## Mechanical comparison

| Detail | Earlier v0.1 | Selected slim v0.2 |
| --- | --- | --- |
| Frame W × D × H | 550 × 360 × 550 mm | 550 × 230 × 677 mm |
| Filters | Two nominal 20 × 20 × 1 in | Two nominal 20 × 25 × 1 in |
| Fans | Six 140 mm, upward exhaust | Six 140 mm, three exhausting from each narrow side |
| Gross nominal filter face area | Baseline | 25% larger; actual media area depends on product |
| Body footprint | Baseline | 36% smaller |
| Footprint with proposed stabilizers | Feet not detailed | 550 × 300 mm, 17% smaller than v0.1 frame footprint |
| Airflow/service tradeoff | Upward outlets, deeper cabinet | Shallower cabinet, side drafts and more surrounding clearance |
| Initial parts allowance | $200–355 | $220–380 per unit |

The slim geometry preserves fan count while increasing filter area. That makes it worth prototyping, but does not prove more CADR or less noise. Side exhaust may recirculate near the adjacent intake faces or be obstructed by furniture; test placement and outlet direction.

The approximate outer envelope with 6 mm panels, 12 mm exterior guard reservations, and 18 mm stabilizer skids is **586 W × 300 D × 707 H mm** (23.1 × 11.8 × 27.8 in), before rubber pads, protruding fasteners or cable connector. The 550 × 230 × 677 figure describes the frame only.

## Air path, maintenance and construction

Both broad faces are filter intakes. Top and bottom are sealed. All six side fans exhaust outward. Filter arrows point into the common plenum.

Filters lift outward after loosening captive edge retainers. They do not slide past the fans, and the top does not need removal for ordinary filter changes. Provide internal blade guards because removing a filter exposes the plenum. Exterior and interior guard volumes are reserved in CAD; the model does not contain functional guards.

Each side fan plate removes as a service module. Use a keyed disconnect and strain relief for its harness, with enough service loop to unplug it without pulling conductors. Keep the controller and distribution wiring in the upper plenum, outside blades and filter removal paths; final brackets and cable routing remain to be modeled.

Use metal brackets for structural frame joints, printed segments for filter seats, and continuous closed-cell gasket strips across segment joins. Retention tabs in CAD illustrate location only. Their screws, captive hardware, compression stops and print orientation are not yet designed.

The nominal side fan centers are Y = 115 mm and Z = 188.5, 338.5, 488.5 mm. Fan body pitch is 150 mm, leaving 10 mm between 140 mm bodies. Current geometry leaves 15 mm between fan bodies and the inner edge of the filter-seat zone. Keep brackets and wiring out of this space.

Provisional cut list: four 677 mm posts, four 510 mm width rails, four 190 mm depth rails; total 5.508 m before kerf. **Do not cut yet:** these depend on illustrative 508 × 635 × 25 mm actual filters and 1 mm clearance per edge.

Two 300 mm-deep skids increase tip resistance, but stability is not validated. Retain them mechanically; attach rubber pads. Assess cable-pull, bump and tip behavior with real mass distribution. Do not treat the closed top as load-bearing furniture.

## H2D printing approach

The [Bambu H2D specification](https://eu.store.bambulab.com/products/h2d?from=home_page_3dprinter) lists 325 × 320 × 325 mm for single-nozzle printing and 300 × 320 × 325 mm for dual-nozzle printing. Use a conservative 280 × 280 mm maximum part footprint to allow for brims and placement; verify each plate in Bambu Studio.

Split long 510 mm seat rails into two segments and 637 mm rails into three. Exact lengths depend on corner overlap and joint details. The 300 mm stabilizers are preferably bought/cut metal or wood; do not assume they must be printed. Fan plates remain sheet material. Begin with a small slot/fastener/gasket coupon after measuring the extrusion, before printing complete fittings.

## Budget and purchasing order

Per-unit planning allowance: filters $45–70; six fans $45–80; power/controller/harness $35–60; metal hardware $25–45; panels $25–45; guards/gaskets/skids/feet $35–55; printed fittings $10–25. Total **$220–380**, excluding existing extrusion, tools, shipping, tax and instruments. Two units: $440–760; three: $660–1,140. These are allowances, not vendor quotes.

First obtain one filter pair and one sample fan to settle dimensions and tonal-noise concerns. Then obtain the remaining fans for a temporary full-array plenum test. Order fleet quantities only after measuring the prototype's useful quiet CADR. Buying two full sets now could duplicate a design that needs revision.

## CAD deliverables and verification

- [Fusion archive](../design/slim-v02/slim-v02.f3d)
- [STEP assembly](../design/slim-v02/slim-v02.step)
- [Model preview](../design/slim-v02/slim-v02.png)
- [Fusion generator](../design/slim-v02/generate_fusion.py)
- [Verification record](../design/slim-v02/verification.json)

This is a direct-model layout study with separately named component groups, not a fully constrained parametric Fusion timeline. Generator inputs support layout exploration; all changes require renewed clearance checks. Frame bars are solid envelopes, filter media are solid stand-ins, fan blades are omitted, and guard reservations are hidden. Mass and airflow cannot be inferred from those simplified bodies.

Checked: frame arithmetic, fan spacing, filter-seat separation, successful solid creation and F3D/STEP export, visual inspection, and Fusion interference analysis excluding guard reservations. The latter found zero positive-volume interferences among the modeled component groups; it does not verify unmodeled joints or fasteners.

Before fabrication: measure actual filters and extrusion; finalize joints, holes, guards, printed segments, wiring and foot attachment; validate stability; then measure noise and particle removal using [the prototype test plan](validation.md).
