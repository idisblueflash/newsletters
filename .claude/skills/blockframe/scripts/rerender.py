"""Re-render the blockout PNG from whatever camera the .blend currently has.
Run:  Blender -b bedroom-blockout.blend --python rerender.py
"""
import bpy
scene = bpy.context.scene
scene.render.filepath = "/Users/husongtao/Projects/newsletters/output/blockout/bedroom-blockout.png"
scene.render.resolution_x = 1568
scene.render.resolution_y = 672
bpy.ops.render.render(write_still=True)
cam = scene.camera
print("CAM_LOC", tuple(round(v, 3) for v in cam.location))
print("CAM_ROT_DEG", tuple(round(__import__('math').degrees(v), 2) for v in cam.rotation_euler))
print("RERENDERED")
