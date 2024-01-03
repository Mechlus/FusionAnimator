import bpy
import json
import os
import math
from collections import OrderedDict
from math import degrees

scene = bpy.context.scene
start_frame = scene.frame_start
end_frame = scene.frame_end

data = OrderedDict()

info_data = OrderedDict()

info_data['minFrame'] = start_frame
info_data['maxFrame'] = end_frame
info_data['easer'] = 1.0
info_data['loop'] = False

data['info'] = info_data

animation_data = OrderedDict()

# loop through selected objects, but should only save last data
for obj in bpy.context.scene.objects:
    if obj.select:
        loc_keyframes = []
        rot_keyframes = []
        scale_keyframes = []

        # loop through frames
        for frame in range(start_frame, end_frame+1):
            scene.frame_set(frame)

            loc = obj.matrix_world.to_translation()
            rot = obj.matrix_world.to_euler()
            scale = obj.matrix_world.to_scale()

            # convert to degrees and round decimal, remove rounding if necessary
            rot = [round(math.degrees(r), 3) for r in rot]

            loc_keyframes.append(list(loc))
            rot_keyframes.append(list(rot))
            scale_keyframes.append(list(scale))

        # add keyframe data
        animation_data["obj"] = {
            'loc': loc_keyframes,
            'rot': rot_keyframes,
            'scale': scale_keyframes
        }
data['animation'] = animation_data

# write animation information
blend_file_path = bpy.data.filepath
blend_file_name = os.path.splitext(os.path.basename(blend_file_path))[0]
data_file_path = os.path.join(os.path.dirname(blend_file_path), 'anim_' + blend_file_name + '.json')
print("Saving animation to " + data_file_path)
with open(data_file_path, 'w') as f:
    json.dump(data, f, indent=4)
