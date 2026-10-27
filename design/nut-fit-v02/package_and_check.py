from pathlib import Path
import zipfile, re, json
p=Path(__file__).resolve().parent
stem='fit-v02_MK4S-MMU3_0p6_PETG-HF'
g=(p/(stem+'.gcode')).read_text()
config=g.split('; prusaslicer_config = begin')[1].split('; prusaslicer_config = end')[0].strip()
assert set(re.findall(r'^T(\d+)\s*$',g,re.M))=={'0'}
assert 'M862.1 P0.6' in g and 'MK4S' in g and 'MMU3' in g
assert '; temperature = 240' in config and '; bed_temperature = 75' in config
for line in config.splitlines():
    if line.startswith(('; printhost_apikey =','; print_host =')): assert not line.split('=',1)[1].strip()
f=p/(stem+'.3mf')
with zipfile.ZipFile(f) as z: entries={n:z.read(n) for n in z.namelist() if n!='Metadata/Slic3r_PE.config'}
with zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as z:
    for n,data in entries.items(): z.writestr(n,data)
    z.writestr('Metadata/Slic3r_PE.config',config+'\n')
print('\n'.join(l for l in g.splitlines() if any(k in l for k in ['estimated printing time','total filament used [g]'])))
# Envelope check uses measured cavity and assumed lip depth 1.8 mm, 45 degree slopes.
# It is NOT a guarantee: floor width and lip depth need physical confirmation.
rows=json.loads((p/'geometry-check.json').read_text())
for r in rows:
    checks=[]
    for z in [i/100 for i in range(321)]:
        depth=5.7-z # 1.8 lip + 3.9 assembled carrier/nut
        cavity=min(11,5.7+2*(6.2-depth))
        width=min(r['width'],r['bottom_width']+2*z)
        checks.append(cavity-width)
    r['inferred_min_total_width_clearance_mm']=round(min(checks),3)
    assert min(checks)>0
    print('Sample',r['sample'],'minimum modeled total clearance',round(min(checks),3))
(p/'geometry-check.json').write_text(json.dumps(rows,indent=2)+'\n')
