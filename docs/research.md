# Research grounding
Checked 2026-10-27. Source measurements apply to the cited configuration only.

## Similar designs

| Approach | Evidence | Implication for this project |
| --- | --- | --- |
| Traditional box-fan Corsi–Rosenthal box | [EPA DIY guidance](https://www.epa.gov/emergencies-iaq/diy-air-cleaners) reports improved CADR with multiple filters, thicker filters and shrouds. [UC Davis WCEC](https://wcec.ucdavis.edu/testing-different-configurations-of-do-it-yourself-portable-air-cleaners/) tested airflow, noise and power and calculated CADR using filter reports. | Good low-cost baseline; a large box fan is less aligned with our quiet cabinet goal. |
| CleanAirKits Luggable XL Ultra | [ENERGY STAR record](https://www.energystar.gov/productfinder/product/certified-room-air-cleaners/details/4020923/export/pdf) lists 333 CFM smoke, 402 CFM dust and 450 CFM pollen CADR; smoke CADR/W is 23.96. | Strong evidence that a multi-PC-fan, large-filter architecture can provide substantial particle cleaning. It does not validate our fan choice or cabinet. |
| CleanAirKits Luggable Ultra family | [Manufacturer specifications](https://www.cleanairkits.com/en-eu/products/luggables-europe) list the five-fan unit at 231 CFM smoke CADR and 37.5 dBA at 1 m; the seven-fan XL lists 39 dBA. | Useful acoustic benchmark. Manufacturer noise figures are not a controlled comparison with our future measurements. |
| Nukit Open Air Purifier | [Original design repository](https://github.com/opennukit/Nukit-Open-Air-Purifier) provides hanging, tower and wall variants using HVAC filters, 140 mm fans, guards and external 12 V power. Its panels use 3 mm sheet material. | Useful serviceability and enclosure precedent. Our extrusion frame is an original concept; no upstream CAD files have been copied. Upstream files are GPL-3.0 and require license review if later reused. |

## Filter and fan lessons

[CleanAirKits' filter comparison](https://www.cleanairkits.com/blogs/news/what-happens-to-cadr-with-different-grade-filters) shows that changing filter grade can change system CADR in either direction. Their salt-aerosol drawdown results are explicitly not AHAM smoke/dust/pollen results. Choose a specific low-resistance MERV 13 product and evaluate the assembled system; MERV alone does not describe pressure drop.

The [ARCTIC P14 PWM PST specification](https://www.arctic.de/en/P14-PWM-PST/) lists 140 × 140 × 27 mm, 12 V, 0.12 A, 200–1700 RPM, 72.8 CFM free-air flow, 2.40 mm water maximum static pressure and 0.3 sone. These apply to the named variant, not P14 Max, Pro, Slim or RGB models. Check the purchased revision. Availability and prices need supplier confirmation.

Free-air flow and shutoff pressure are opposite ends of a fan curve, not simultaneous operating values. Six parallel fans increase flow capacity; their pressure ratings do not add. Multiplying 72.8 CFM by six does not give purifier CADR. Sone ratings cannot be directly compared to in-room dBA readings without matching conditions.

## Scope and sizing

[EPA household guidance](https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home) sizes particle filtration by CADR and distinguishes it from gas filtration. Its table gives 195 CFM for 300 ft² at an 8 ft ceiling. This project rounds to a 200 CFM target, equivalent to five clean-air changes per hour for that room.

MERV 13 filtration addresses airborne particles, including dust, pollen and smoke particles. It does not solve CO₂ buildup, carbon monoxide, or general VOC/odor problems. Meaningful gas filtration would require a separate sorbent design and pressure budget. Version 1 therefore uses mechanical particle filtration only.

## Design decision

Start with a two-filter PC-fan cabinet. It balances filter area, footprint and access, uses the available extrusion, and can be built from straight cuts and printed adapters. A four-filter cube is the fallback if measured resistance prevents reaching the noise/CADR goal. A blower plus HEPA cartridge remains an alternative if footprint becomes the overriding constraint; it needs a different pressure and acoustic design.

Use CADR at the chosen quiet operating speed to judge success. Do not pair maximum-speed CADR with minimum-speed noise.
