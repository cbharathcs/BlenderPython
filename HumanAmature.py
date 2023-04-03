import bpy

# Get the armature object and the head bone
armature = bpy.data.objects['Armature']
head_bone = armature.pose.bones['head']

# Set the frame range for the animation
start_frame = 1
end_frame = 100

# Set the keyframe for the mouth open and closed positions
mouth_open = 0.2
mouth_closed = 0.0
head_bone.rotation_quaternion.keyframe_points.insert(
    frame=start_frame, value=mouth_closed)
head_bone.rotation_quaternion.keyframe_points.insert(
    frame=end_frame, value=mouth_closed)
head_bone.rotation_quaternion.keyframe_points.insert(
    frame=start_frame + (end_frame - start_frame) // 2, value=mouth_open)

# Animate the mouth movements
for frame_num in range(start_frame, end_frame + 1):
    bpy.context.scene.frame_set(frame_num)
    if frame_num <= start_frame + (end_frame - start_frame) // 2:
        head_bone.rotation_quaternion.w = mouth_closed + (mouth_open - mouth_closed) * 2 * (frame_num - start_frame) / (end_frame - start_frame)
    else:
        head_bone.rotation_quaternion.w = mouth_open + (mouth_closed - mouth_open) * 2 * (frame_num - start_frame - (end_frame - start_frame) // 2) / (end_frame - start_frame)

    head_bone.keyframe_insert(data_path="rotation_quaternion")
