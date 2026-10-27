"""Generate three end-loading M5 nut-carrier FIT SAMPLES in Fusion.
All dimensions mm. Metal nut required. Not rated for structural connections.
"""
import math, json
from pathlib import Path
OUT=Path(r"C:\Users\mason\Documents\Air Purifier Design\design\nut-fit-v01")
WIDTHS=[10.0,10.5,11.0]
def run(_context):
    import adsk.core, adsk.fusion
    app=adsk.core.Application.get()
    doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name="M5 nut carrier fit samples v0.1"
    design=adsk.fusion.Design.cast(app.activeProduct)
    design.designType=adsk.fusion.DesignTypes.DirectDesignType
    root=design.rootComponent
    mgr=adsk.fusion.TemporaryBRepManager.get()
    OUT.mkdir(parents=True,exist_ok=True)
    def p(x,y,z): return adsk.core.Point3D.create(x/10,y/10,z/10)
    def box(x,y,z,dx,dy,dz,angle=0):
        a=math.radians(angle)
        return mgr.createBox(adsk.core.OrientedBoundingBox3D.create(
            p(x,y,z),adsk.core.Vector3D.create(math.cos(a),math.sin(a),0),
            adsk.core.Vector3D.create(-math.sin(a),math.cos(a),0),
            dx/10,dy/10,dz/10))
    def boolean(a,b,kind):
        assert mgr.booleanOperation(a,b,kind)
        return a
    cut=adsk.fusion.BooleanTypes.DifferenceBooleanType
    union=adsk.fusion.BooleanTypes.UnionBooleanType
    intersection=adsk.fusion.BooleanTypes.IntersectionBooleanType
    def cyl(x,y,z,h,r):
        return mgr.createCylinderOrCone(p(x,y,z),r/10,p(x,y,z+h),r/10)
    report=[]
    for n,width in enumerate(WIDTHS,1):
        cx=(n-1)*26
        occ=root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        comp=occ.component
        name="carrier_"+str(n)+"_width_"+str(width).replace(".","p")
        comp.name=name
        body=box(cx,0,2.1,18,width,4.2)
        for xx in [-7,7]:
            body=boolean(body,box(cx+xx,0,4.7,4,6.0,1.0),union)
        # Open-top hex pocket with 0.4 mm retaining floor. A 4 mm nut stands 0.2 mm proud.
        pocket=box(cx,0,3.2,20,8.3,5.6)
        for angle in [60,120]:
            pocket=boolean(pocket,box(cx,0,3.2,20,8.3,5.6,angle),intersection)
        body=boolean(body,pocket,cut)
        body=boolean(body,cyl(cx,0,-0.1,7,2.75),cut)
        # One, two, three shallow identification dots on underside near one end.
        for j in range(n):
            body=boolean(body,cyl(cx+7,2*(j-(n-1)/2),-0.1,0.5,0.5),cut)
        b=comp.bRepBodies.add(body)
        b.name=name+" FIT ONLY"
        assert b.isSolid
        stl=design.exportManager.createSTLExportOptions(comp,str(OUT/(name+".stl")))
        stl.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        stl.isBinaryFormat=True
        assert design.exportManager.execute(stl)
        report.append(dict(name=name,width_mm=width,length_mm=18,body_height_mm=4.2,
            guide_width_mm=6.0,total_height_mm=5.2,pocket_across_flats_mm=8.3,
            pocket_depth_mm=3.8,screw_clearance_diameter_mm=5.5,
            volume_mm3=b.volume*1000,solid=b.isSolid))
    exports=design.exportManager
    assert exports.execute(exports.createFusionArchiveExportOptions(str(OUT/"nut-fit-v01.f3d")))
    assert exports.execute(exports.createSTEPExportOptions(str(OUT/"nut-fit-v01.step")))
    stl=exports.createSTLExportOptions(root,str(OUT/"three-carriers.stl"))
    stl.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    assert exports.execute(stl)
    camera=app.activeViewport.camera
    camera.viewOrientation=adsk.core.ViewOrientations.IsoTopRightViewOrientation
    camera.isFitView=True
    app.activeViewport.camera=camera
    app.activeViewport.fit()
    adsk.doEvents()
    assert app.activeViewport.saveAsImageFile(str(OUT/"nut-fit-v01.png"),1400,900)
    (OUT/"geometry-check.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report))
