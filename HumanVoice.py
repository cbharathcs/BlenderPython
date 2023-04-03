import bpy
from mathutils import Euler

# Create new scene
scene = bpy.context.scene

# Add human model to the scene
human_obj = bpy.data.armatures["Armature"]


print("tset >>>",human_obj)


# Define mouth bones
root_bone = human_obj.bones['root']
head_bone = human_obj.bones['head']
jaw_bone = human_obj.bones['jaw']
tongue_bone = human_obj.bones['lip bot']

# Define mouth shapes
mouth_shapes = {
    'A': {'jaw': Euler((0.0, 0.0, 2.0), 'XYZ'), 'tongue': Euler((0.0, -1.0, 0.0), 'XYZ')},
    'E': {'jaw': Euler((0.0, 0.0, 0.0), 'XYZ'), 'tongue': Euler((0.0, 0.0, 0.0), 'XYZ')},
    'I': {'jaw': Euler((0.0, 0.0, 0.0), 'XYZ'), 'tongue': Euler((0.0, 0.0, 0.0), 'XYZ')},
    'O': {'jaw': Euler((0.0, 0.0, 0.0), 'XYZ'), 'tongue': Euler((0.0, 0.0, 0.0), 'XYZ')},
    'U': {'jaw': Euler((0.0, 0.0, 0.0), 'XYZ'), 'tongue': Euler((0.0, 0.0, 0.0), 'XYZ')}
}

bpy.context.scene.tool_settings.use_keyframe_insert_auto = True


def animate_mouth(text):
    # Loop through each character in the text
    for i, char in enumerate(text):
        # Get the mouth shape for the current character
        mouth_shape = mouth_shapes[char.upper()]

        # Set the bone rotations for the current mouth shape
        jaw_bone = mouth_shape['jaw']f
        tongue_bone = mouth_shape['tongue']

        # Set the frame for the current mouth shape
        frame = i + 1
        #jaw_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
        #tongue_bone.keyframe_insert(data_path="rotation_euler", frame=frame)

animate_mouth("AEIOU")


#https://www.youtube.com/watch?v=6nmT123wVe4