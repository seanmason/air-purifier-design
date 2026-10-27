# Prototype validation

No measured performance yet. Record CADR and noise at the **same fan setting**.

## Before fabrication
Confirm room dimensions and connected open spaces; pollutant priorities; maximum size and budget; acceptable night noise; actual filter SKU/dimensions; extrusion slot and available lengths; printer bed and filament. These are open decisions, not approved constraints.

## Bench checks

- Check polarity, secure connectors, strain relief, fan startup at every intended setting and controller current capacity.

- With filters fitted, verify inward intake on both sides and upward exhaust. Check gasket contact and bypass using thin tissue strips, not smoke.

- Inspect wiring/guards and panel temperatures during an attended extended run at full output.

- Check stability, feet, cable snag resistance, filter retention and repeatable servicing.

## Acoustic sweep
Measure at 1 m from the cabinet, at a fixed height, in several directions. Record room/background sound, distance, fan RPM/PWM, meter model, LAeq duration, power and subjective tonal/rattle observations. Use a calibrated low-noise sound meter if claiming a 30–35 dBA result; a phone can compare settings but does not establish that accuracy.

Report purifier-on and background levels. If their difference is small (roughly under 3 dB), the result is background-limited. Do not claim a precise purifier-only value. Record whether the sound is acceptable at the intended bed/desk location as well.

## Cleaning performance
Airflow alone is not CADR. A hood can add resistance; a single outlet velocity reading times fan area is not a defensible airflow measurement because velocity varies and fan hubs block area.

For a practical comparative particle-decay test:

1. Use a measured room volume with doors/windows, HVAC state and mixing held consistent.
2. Log naturally elevated particle concentrations during comparable purifier-off and purifier-on periods. Do not deliberately generate smoke or combustion particles indoors. If background is too low, defer the test or arrange appropriate controlled testing.
3. Fit exponential decay only where concentration is well above sensor noise, sources are absent and mixing is adequate. For constant nonzero background, fit C(t) = Cbackground + A exp(−kt); do not blindly log raw concentration.
4. With k in hours⁻¹ and room volume in ft³, estimate CADR = (k_on − k_off) × volume ÷ 60.
5. Repeat trials and retain raw data, fitting interval, residuals and uncertainty. Outdoor changes, infiltration, inconsistent mixing and optical sensor humidity response can invalidate the result.

This is a field estimate for the measured aerosol/sensor, not an AHAM-certified smoke CADR. Formal claims require appropriate standardized testing.

For 2,400 ft³, a net decay-rate difference of 5/hour corresponds to 200 CFM. At that same setting, the initial goal is ≤35 dBA at 1 m. A failure calls for a design change, not relabeling maximum fan CFM as clean air.

## Iteration decisions
If too loud: investigate grille turbulence, panel resonance and motor tones; lower RPM only while checking cleaning performance. Consider more filter area or more fans at lower speed.

If cleaning is inadequate: first check leakage, fan direction and real filter resistance. Compare a lower-resistance MERV 13 SKU or a larger/four-filter cabinet. Higher filter efficiency is not automatically higher CADR.

Recheck after adding cosmetic panels or changing filters. Inspect filters initially each month and replace based on loading, damage, airflow loss and manufacturer guidance rather than a promised fixed service life.

## Data record
For each trial retain date, room volume, filter SKU/age, cabinet revision, fan/controller settings, background and on-state dBA, watts, sensor details, particle time series, fit method, estimated CADR and limitations. No numerical performance should be marked verified without these records.
