"""Embed the verified G-code configuration into PrusaSlicer's geometry-only CLI 3MF.
PrusaSlicer 2.9.6 uses semicolon-prefixed config lines in Metadata/Slic3r_PE.config.
No third-party dependencies. Retains the geometry and placement from the CLI export.
"""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent
template = root / "fit-samples_MK4S-MMU3_0p4_PETG.3mf"
with zipfile.ZipFile(template) as archive:
    entries = {name: archive.read(name) for name in archive.namelist()
               if name != "Metadata/Slic3r_PE.config"}
for stem in ["fit-samples_MK4S-MMU3_0p4_PETG",
             "fit-samples_MK4S-MMU3_0p6_Bambu-PETG-HF"]:
    gcode = (root / (stem + ".gcode")).read_text(encoding="utf-8")
    config = gcode.split("; prusaslicer_config = begin", 1)[1].split(
        "; prusaslicer_config = end", 1)[0].strip()
    assert "; printer_settings_id =" in config
    assert "; nozzle_diameter =" in config
    for line in config.splitlines():
        if line.startswith(("; printhost_apikey =", "; print_host =")):
            assert not line.split("=", 1)[1].strip(), "Do not package credentials"
    with zipfile.ZipFile(root / (stem + ".3mf"), "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in entries.items():
            archive.writestr(name, data)
        archive.writestr("Metadata/Slic3r_PE.config", config + "\n")
    with zipfile.ZipFile(root / (stem + ".3mf")) as archive:
        assert archive.testzip() is None
    print("Packaged", stem)
