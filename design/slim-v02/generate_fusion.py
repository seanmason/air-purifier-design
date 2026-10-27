"""Fusion layout generator, v0.2. Units in source are millimeters.
Run in Fusion through run(context). Run --check in ordinary Python for layout checks.
Direct-model envelope study, not a fabrication-ready parametric timeline.
"""
import json
import os
from pathlib import Path

OUT = Path(r"C:\Users\mason\Documents\Air Purifier Design\design\slim-v02")
P = dict(filter_w=508.0, filter_h=635.0, filter_t=25.0,
         clearance=1.0, extrusion=20.0, depth=230.0,
         fan_size=140.0, fan_t=27.0, fan_pitch=150.0,
         panel_t=6.0, foot_depth=300.0, foot_height=18.0)

def dimensions():
    e, c = P["extrusion"], P["clearance"]
    return P["filter_w"]+2*c+2*e, P["depth"], P["filter_h"]+2*c+2*e

def check_layout():
    w,d,h = dimensions()
    centers = [h/2-P["fan_pitch"], h/2, h/2+P["fan_pitch"]]
    half = P["fan_size"]/2
    assert d/2-half > P["filter_t"]+5, "Fan overlaps filter seat zone"
    assert centers[0]-half > P["extrusion"]+25, "Bottom bracket clearance"
    assert centers[-1]+half < h-P["extrusion"]-25, "Top bracket clearance"
    assert P["fan_pitch"] > P["fan_size"], "Fan bodies touch"
    assert w-2*P["fan_t"] > 0
    assert P["foot_depth"] >= d
    return dict(frame_mm=[w,d,h], fan_centers_z_mm=centers,
                nominal_filter_face_area_ratio_to_v01=P["filter_h"]/508,
                frame_footprint_reduction_vs_v01=1-d/360,
                foot_footprint_reduction_vs_v01=1-P["foot_depth"]/360,
                extrusion_net_m=4*(h+w-40+d-40)/1000,
                fan_to_filter_seat_gap_mm=d/2-half-(P["filter_t"]+5))

def run(_context):
    import adsk.core, adsk.fusion
    report = check_layout()
    OUT.mkdir(parents=True, exist_ok=True)
    app = adsk.core.Application.get()
    doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name = "Quiet purifier - slim v0.2 - layout study"
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.DirectDesignType
    root = design.rootComponent
    mgr = adsk.fusion.TemporaryBRepManager.get()
    def pt(x,y,z):
        return adsk.core.Point3D.create(x/10,y/10,z/10)
    def box(x,y,z,dx,dy,dz):
        bounds = adsk.core.OrientedBoundingBox3D.create(
            pt(x+dx/2,y+dy/2,z+dz/2),
            adsk.core.Vector3D.create(1,0,0), adsk.core.Vector3D.create(0,1,0),
            dx/10,dy/10,dz/10)
        return mgr.createBox(bounds)
    def cylinder(x1,y1,z1,x2,y2,z2,r):
        return mgr.createCylinderOrCone(pt(x1,y1,z1),r/10,pt(x2,y2,z2),r/10)
    def cut(body,tool):
        assert mgr.booleanOperation(body,tool,adsk.fusion.BooleanTypes.DifferenceBooleanType)
        return body
    def component(name):
        comp=root.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        comp.name=name
        return comp
    counts={}
    def add(comp,name,body):
        b=comp.bRepBodies.add(body)
        assert b and b.isSolid, name
        b.name=name
        counts[comp.name]=counts.get(comp.name,0)+1
        return b
    def ring_y(x,y,z,w,t,h,rim):
        return cut(box(x,y,z,w,t,h),box(x+rim,y-1,z+rim,w-2*rim,t+2,h-2*rim))

    w,d,h=dimensions()
    frame=component("01 Frame - solid 2020 envelopes; slots and joints not modeled")
    for x in [0,w-20]:
        for y in [0,d-20]:
            add(frame,"Post 677 nominal",box(x,y,0,20,20,h))
    for z in [0,h-20]:
        for y in [0,d-20]:
            add(frame,"Width rail 510 nominal",box(20,y,z,w-40,20,20))
        for x in [0,w-20]:
            add(frame,"Depth rail 190 nominal",box(x,20,z,20,d-40,20))
    panels=component("02 Panels - provisional 134 mm fan openings; no fastener holes")
    add(panels,"Top",box(0,0,h,w,d,6))
    add(panels,"Bottom",box(0,0,-6,w,d,6))
    for side,x in [("Left",-6),("Right",w)]:
        b=box(x,0,0,6,d,h)
        for z in report["fan_centers_z_mm"]:
            b=cut(b,cylinder(x-1,d/2,z,x+7,d/2,z,67))
        add(panels,side+" removable fan plate",b)
    filters=component("03 Filters - illustrative 508 x 635 x 25; actual SKU required")
    for name,y in [("Front",0),("Rear",d-25)]:
        add(filters,name+" cardboard rim envelope",ring_y(21,y,21,508,25,635,15))
        add(filters,name+" media envelope; pleats not modeled",box(36,y+2,36,478,21,605))
    seats=component("04 Continuous filter seats and gaskets - segment joints unresolved")
    for name,y in [("Front",27),("Rear",d-30)]:
        add(seats,name+" shoulder",ring_y(20,y,20,w-40,3,h-40,11))
    for name,y in [("Front",25),("Rear",d-27)]:
        add(seats,name+" compressed gasket envelope",ring_y(21,y,21,508,2,635,10))
    fans=component("05 Six side-exhaust fans - simplified envelopes, not vendor CAD")
    for side,x in [("Left",0),("Right",w-27)]:
        for i,z in enumerate(report["fan_centers_z_mm"],1):
            b=box(x,d/2-70,z-70,27,140,140)
            b=cut(b,cylinder(x-1,d/2,z,x+28,d/2,z,66))
            add(fans,side+" fan "+str(i)+" frame",b)
            add(fans,side+" fan "+str(i)+" hub envelope",cylinder(x,d/2,z,x+27,d/2,z,19))
    retainers=component("06 Filter retention tabs - illustrative only; no screws")
    for side,y in [("Front",-4),("Rear",d)]:
        for x in [10,w-34]:
            for z in [120,h-145]:
                add(retainers,side+" edge tab",box(x,y,z,24,4,25))
    feet=component("07 Stabilizer skids - 300 mm depth; rubber pads and attachment unresolved")
    for x in [80,w-110]:
        add(feet,"Stabilizer skid",box(x,(d-300)/2,-24,30,300,18))
    # Explicit keep-out envelopes, hidden so they cannot be mistaken for guards.
    guards=component("08 Guard keep-outs ONLY - purchase guards; finger protection not modeled")
    for x in [-18,w+6]:
        for z in report["fan_centers_z_mm"]:
            add(guards,"Exterior guard reservation",box(x,d/2-72,z-72,12,144,144))
    for x in [27,w-35]:
        for z in report["fan_centers_z_mm"]:
            add(guards,"Interior guard reservation",box(x,d/2-72,z-72,8,144,144))
    guards.isBodiesFolderLightBulbOn=False
    entities=adsk.core.ObjectCollection.create()
    for occ in root.occurrences:
        if not occ.component.name.startswith("08 "):
            for body in occ.component.bRepBodies:
                entities.add(body.createForAssemblyContext(occ))
    interference_input=design.createInterferenceInput(entities)
    interference_input.areCoincidentFacesIncluded=False
    interference=design.analyzeInterference(interference_input)
    report["interference_checked_body_count"]=entities.count
    report["positive_volume_interference_pairs_excluding_guard_keepouts"]=[
        [interference.item(i).entityOne.name,interference.item(i).entityTwo.name]
        for i in range(interference.count)]
    assert interference.count == 0, "Resolve physical body interference before export"
    camera=app.activeViewport.camera
    camera.viewOrientation=adsk.core.ViewOrientations.IsoTopRightViewOrientation
    camera.isFitView=True
    app.activeViewport.camera=camera
    app.activeViewport.fit()
    adsk.doEvents()
    exports=design.exportManager
    assert exports.execute(exports.createFusionArchiveExportOptions(str(OUT/"slim-v02.f3d")))
    assert exports.execute(exports.createSTEPExportOptions(str(OUT/"slim-v02.step")))
    assert app.activeViewport.saveAsImageFile(str(OUT/"slim-v02.png"),1500,1100)
    report["body_counts"]=counts
    report["model_type"]="Direct-model geometric layout; generator parameters are source of truth"
    report["unmodeled"]="Slots, brackets, fasteners, cables, real guards, pleats, print segmentation"
    (OUT/"verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__":
    import sys
    if "--check" in sys.argv:
        print(json.dumps(check_layout(),indent=2))
