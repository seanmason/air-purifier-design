"""Chamfered, end-loading M5 THIN-nut carriers. Dimensions in mm.
Measured cavity: 11 wide, 6.2 deep, approximately 5.7 floor width.
Nut envelope assumes M5 8 AF x 2.7 thick; ordinary 4 mm nuts are NOT suitable.
"""
import math, json
from pathlib import Path
OUT=Path(r"C:\Users\mason\Documents\Air Purifier Design\design\nut-fit-v02")
SAMPLES=[(1,10.0,2.0),(2,10.4,2.0),(3,10.8,2.2),(4,10.4,2.3)]

def run(_context):
    import adsk.core, adsk.fusion
    app=adsk.core.Application.get()
    doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name='Chamfered M5 thin-nut fit samples v02'
    design=adsk.fusion.Design.cast(app.activeProduct)
    design.designType=adsk.fusion.DesignTypes.DirectDesignType
    root=design.rootComponent
    mgr=adsk.fusion.TemporaryBRepManager.get()
    def p(x,y,z): return adsk.core.Point3D.create(x/10,y/10,z/10)
    def box(x,y,z,dx,dy,dz,angle=0):
        a=math.radians(angle)
        return mgr.createBox(adsk.core.OrientedBoundingBox3D.create(p(x,y,z),
            adsk.core.Vector3D.create(math.cos(a),math.sin(a),0),
            adsk.core.Vector3D.create(-math.sin(a),math.cos(a),0),dx/10,dy/10,dz/10))
    def boolean(a,b,kind):
        assert mgr.booleanOperation(a,b,kind)
        return a
    cut=adsk.fusion.BooleanTypes.DifferenceBooleanType
    union=adsk.fusion.BooleanTypes.UnionBooleanType
    inter=adsk.fusion.BooleanTypes.IntersectionBooleanType
    def cyl(x,y,z,h,r): return mgr.createCylinderOrCone(p(x,y,z),r/10,p(x,y,z+h),r/10)
    report=[]
    for n,width,bevel in SAMPLES:
        cx=(n-1)*25
        comp=root.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        comp.name=f'Sample_{n}_W{width}_bevel{bevel}'
        # XZ sketch coordinates map local x to world x; create cross-section on YZ.
        sk=comp.sketches.add(comp.yZConstructionPlane)
        # Use modelToSketchSpace rather than assume the construction-plane axes.
        yz=[(-width/2+bevel,0),(width/2-bevel,0),(width/2,bevel),
            (width/2,3.2),(-width/2,3.2),(-width/2,bevel)]
        pts=[sk.modelToSketchSpace(p(0,y,z)) for y,z in yz]
        for a,b in zip(pts,pts[1:]+pts[:1]): sk.sketchCurves.sketchLines.addByTwoPoints(a,b)
        ext=comp.features.extrudeFeatures.addSimple(sk.profiles.item(0),
            adsk.core.ValueInput.createByReal(1.8),adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        base=ext.bodies.item(0)
        # Center in X, position sample on plate.
        body=mgr.copy(base)
        mat=adsk.core.Matrix3D.create(); mat.translation=adsk.core.Vector3D.create((cx-9)/10,0,0)
        assert mgr.transform(body,mat)
        base.deleteMe(); sk.isVisible=False
        # 0.8 tall end guides: nothing enclosing or restricting the nut above its pocket.
        for xx in [-7,7]: body=boolean(body,box(cx+xx,0,3.6,4,5.8,0.8),union)
        # Thin nut pocket: 1.2 floor, 2.0 deep. 2.7 nut stands 0.7 proud.
        pocket=box(cx,0,3.7,20,8.3,5)
        for angle in [60,120]: pocket=boolean(pocket,box(cx,0,3.7,20,8.3,5,angle),inter)
        body=boolean(body,pocket,cut)
        body=boolean(body,cyl(cx,0,-0.1,7,2.75),cut)
        # Readable 1-4 dots on top of one end guide, diameter 1.2, pitch 1.5.
        for j in range(n): body=boolean(body,cyl(cx+7,(j-(n-1)/2)*1.5,3.6,0.6,0.6),cut)
        b=comp.bRepBodies.add(body); b.name=comp.name+' FIT ONLY'
        assert b.isSolid
        opts=design.exportManager.createSTLExportOptions(comp,str(OUT/(comp.name+'.stl')))
        opts.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        assert design.exportManager.execute(opts)
        report.append(dict(sample=n,width=width,lower_corner_45deg_bevel=bevel,
            bottom_width=width-2*bevel,body_height=3.2,guide_width=5.8,overall_height=4.0,
            nut_pocket_AF=8.3,pocket_depth=2.0,floor=1.2,metal_nut_thickness=2.7,
            assembled_height=3.9,volume_mm3=b.volume*1000,solid=b.isSolid))
    ex=design.exportManager
    assert ex.execute(ex.createFusionArchiveExportOptions(str(OUT/'nut-fit-v02.f3d')))
    assert ex.execute(ex.createSTEPExportOptions(str(OUT/'nut-fit-v02.step')))
    opts=ex.createSTLExportOptions(root,str(OUT/'four-carriers.stl'))
    opts.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    assert ex.execute(opts)
    cam=app.activeViewport.camera; cam.viewOrientation=adsk.core.ViewOrientations.IsoTopRightViewOrientation
    cam.isFitView=True; app.activeViewport.camera=cam; app.activeViewport.fit(); adsk.doEvents()
    app.activeViewport.saveAsImageFile(str(OUT/'nut-fit-v02.png'),1400,900)
    (OUT/'geometry-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

