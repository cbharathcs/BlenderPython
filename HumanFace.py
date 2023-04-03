import bpy

# Create new mesh
mesh_data = bpy.data.meshes.new(name="HumanMesh")
mesh_obj = bpy.data.objects.new(name="HumanModel", object_data=mesh_data)
bpy.context.collection.objects.link(mesh_obj)

# Create vertices
verts = [
    (-1.0, -1.0, 0.0),
    (1.0, -1.0, 0.0),
    (1.0, 1.0, 0.0),
    (-1.0, 1.0, 0.0),
    (0.0, 0.0, 2.0)
]

# Create faces
faces = [
    (0, 1, 2, 3),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
]

# Link vertices and faces to mesh
mesh_data.from_pydata(verts, [], faces)
mesh_data.update()

# Set shading to smooth
mesh_obj.data.use_auto_smooth = True
mesh_obj.data.auto_smooth_angle = 60