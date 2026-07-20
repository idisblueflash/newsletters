"""
blockframe blockout TEMPLATE — edit per scene; the attic bedroom below is a
worked example (dimensioned from a Nano Banana blueprint: room 4.8 x 3.2 m,
walls 2.8 m, sloped ceiling 25 deg, window sill 0.9 m).

Method: build the room shell + one flat COLOR-CODED primitive mass per object
(BoxCtrl-style — the render doubles as a labeled structure guide), set a camera,
and render a flat 21:9 greybox. All geometry/camera iteration happens here
because it is free and ~1 s per render. Keep one color <-> one object; mirror the
same mapping in references/style-mapping-prompt.md so Nano Banana knows what each
color becomes.

Run headless:
  /Applications/Blender.app/Contents/MacOS/Blender --background --python blockout_template.py
Then open the saved .blend for the human to set the camera (Lock-Camera-to-View
is enabled), and re-render with rerender.py.
"""
import bpy, mathutils, math, os

OUT   = "/Users/husongtao/Projects/newsletters/output/blockout/bedroom-blockout.png"
BLEND = "/Users/husongtao/Projects/newsletters/output/blockout/bedroom-blockout.blend"

# ---- blueprint dimensions (meters) ----
W, D, H = 4.8, 3.2, 2.8        # room width(x), depth(y), wall height(z)
SILL, WIN_H = 0.9, 1.3         # window sill height, window height
SLOPE = math.radians(25)       # attic ceiling slope

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
world = bpy.data.worlds.new("W"); world.use_nodes = False
world.color = (0.62, 0.62, 0.62); scene.world = world

def mat(n, c):
    m = bpy.data.materials.new(n); m.use_nodes = False; m.diffuse_color = c; return m
C = {
    "wall": mat("wall",(.55,.55,.55,1)), "floor": mat("floor",(.42,.42,.42,1)),
    "ceiling": mat("ceiling",(.12,.12,.14,1)), "bed": mat("bed",(.85,.15,.15,1)),
    "sleeper": mat("sleeper",(.80,.75,.92,1)), "window": mat("window",(.15,.35,.90,1)),
    "curtain": mat("curtain",(.55,.30,.65,1)), "wardrobe": mat("wardrobe",(.15,.70,.25,1)),
    "desk": mat("desk",(.95,.55,.10,1)), "laptop": mat("laptop",(.20,.85,.90,1)),
    "owl": mat("owl",(.85,.20,.80,1)),
}
def box(n,loc,sz,m):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.active_object
    o.name=n; o.scale=(sz[0]/2,sz[1]/2,sz[2]/2); o.data.materials.append(C[m]); return o
def plane(n,loc,sz,rot,m):
    bpy.ops.mesh.primitive_plane_add(location=loc); o=bpy.context.active_object
    o.name=n; o.scale=(sz[0]/2,sz[1]/2,1); o.rotation_euler=rot; o.data.materials.append(C[m]); return o
def cyl(n,loc,r,h,m):
    bpy.ops.mesh.primitive_cylinder_add(location=loc,radius=r,depth=h); o=bpy.context.active_object
    o.name=n; o.data.materials.append(C[m]); return o

# ---- room shell (window/wardrobe on the LEFT wall x=0; bed along the FRONT y~0) ----
plane("floor",     (W/2, D/2, 0),     (W+0.6, D+0.6), (0,0,0), "floor")
plane("wall_left", (0, D/2, H/2),     (D+0.6, H),     (0, math.radians(90), 0), "wall")
plane("wall_back", (W/2, D, H/2),     (W+0.6, H),     (math.radians(90), 0, 0), "wall")
# flat ceiling over the left (tall) half, then a 25-deg slope descending to the right
plane("ceil_flat", (1.1, D/2, H),     (2.2, D+0.6),   (0,0,0), "ceiling")
run = W - 2.2                                   # slope runs from x=2.2 to x=W
plane("ceil_slope",(2.2+run/2, D/2, H-0.5*run*math.tan(SLOPE)),
      (run/math.cos(SLOPE), D+0.6), (0, SLOPE, 0), "ceiling")

# ---- objects ----
box("wardrobe", (0.35, 0.55, 0.95), (0.6, 1.0, 1.9), "wardrobe")
# two-pane casement window on the left wall
plane("window_L", (0.03, 1.24, SILL+WIN_H/2), (0.5, WIN_H), (0, math.radians(90), 0), "window")
plane("window_R", (0.03, 1.76, SILL+WIN_H/2), (0.5, WIN_H), (0, math.radians(90), 0), "window")
# curtains drawn back to each side
box("curtain_L", (0.13, 0.85, 1.6), (0.2, 0.22, 2.2), "curtain")
box("curtain_R", (0.13, 2.15, 1.6), (0.2, 0.22, 2.2), "curtain")
# owl on the sill
cyl("owl", (0.18, 1.5, SILL+0.15), 0.09, 0.28, "owl")
# desk + laptop, center-back
box("desk_top", (2.3, 2.35, 0.72), (1.0, 0.5, 0.06), "desk")
box("desk_l1",  (1.85, 2.15, 0.36), (0.06,0.06,0.72), "desk")
box("desk_l2",  (2.75, 2.15, 0.36), (0.06,0.06,0.72), "desk")
box("laptop",   (2.3, 2.42, 0.9),  (0.36, 0.04, 0.24), "laptop")
# bed spanning the front, sleeper on the right, pillow far right
box("bed",     (2.5, 0.85, 0.28), (4.0, 1.2, 0.4), "bed")
box("sleeper", (3.7, 0.85, 0.52), (1.6, 0.9, 0.36), "sleeper")
box("pillow",  (4.35, 0.85, 0.46),(0.5, 0.9, 0.3), "bed")

# ---- camera: front-right, eye-level, looking across toward the window ----
cd = bpy.data.cameras.new("Cam"); cam = bpy.data.objects.new("Cam", cd)
scene.collection.objects.link(cam)
cam.location = (6.6, -3.0, 2.05)
d = mathutils.Vector((1.4, 1.7, 1.05)) - cam.location
cam.rotation_euler = d.to_track_quat('-Z','Y').to_euler()
cd.lens = 24; scene.camera = cam

# ---- flat color render, 21:9 ----
scene.render.engine = 'BLENDER_WORKBENCH'
scene.display.shading.light = 'FLAT'; scene.display.shading.color_type = 'MATERIAL'
scene.render.resolution_x = 1568; scene.render.resolution_y = 672
scene.render.filepath = OUT
os.makedirs(os.path.dirname(OUT), exist_ok=True)
bpy.ops.render.render(write_still=True); print("WROTE", OUT)
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            for sp in area.spaces:
                if sp.type == 'VIEW_3D':
                    sp.lock_camera = True; sp.shading.type='SOLID'
                    sp.shading.light='FLAT'; sp.shading.color_type='MATERIAL'
                    if sp.region_3d: sp.region_3d.view_perspective='CAMERA'
bpy.ops.wm.save_as_mainfile(filepath=BLEND); print("WROTE_BLEND", BLEND)
