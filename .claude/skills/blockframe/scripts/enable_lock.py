"""Enable 'Lock Camera to View' + camera perspective + flat material shading
directly in the .blend's stored screens (works in background mode), then re-save."""
import bpy
BLEND = "/Users/husongtao/Projects/newsletters/output/blockout/bedroom-blockout.blend"
n = 0
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            for sp in area.spaces:
                if sp.type == 'VIEW_3D':
                    sp.lock_camera = True
                    sp.shading.type = 'SOLID'
                    sp.shading.light = 'FLAT'
                    sp.shading.color_type = 'MATERIAL'
                    if sp.region_3d:
                        sp.region_3d.view_perspective = 'CAMERA'
                    n += 1
print("PATCHED_VIEW3D_SPACES", n)
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
print("RESAVED")
