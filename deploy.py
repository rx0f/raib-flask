import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import json
from PIL import Image
from mayavi import mlab
import cv2
import os
from Util import *
from Framelets import *
from JitterCorrection import *
from Vis3D import *
from ColorCorrection import *

if os.path.exists('dep1.png'):
    os.remove('dep1.png')

image = 'raw.png'
im_info = 'raw.json'
with open(im_info, 'rb') as json_file:
    im_info_dir = json.load(json_file)

img = Image.open(image)
im_ar = np.array(img)
s1, s2 = im_ar.shape


start_time = im_info_dir["START_TIME"]
frame_delay = float(im_info_dir["INTERFRAME_DELAY"].split()[0])+0.001

start_correction, frame_delay = correct_image_start_time_and_frame_delay(im_ar, start_time, frame_delay)

framelets = generate_framelets(revert_square_root_encoding(im_ar), start_time, start_correction, frame_delay)

cam_pos, cam_orient = get_junocam_jupiter_rel_pos_orient(start_time, start_correction + 17 * frame_delay)

y, x = np.mgrid[-512:512,-512:512]
x += 260
y += 95
rays = np.concatenate([x[...,None], y[...,None], np.ones((1024,1024,1))*fl[0]], axis=-1)
rays = rays.dot(cam_orient)

surface_raster, _ = project_onto_jupiter_surf(cam_pos, rays)

colors = np.zeros((1024,1024,3))
color_counts = np.zeros((1024,1024,3))

for k,framelet in enumerate(framelets):
    col = framelet.color
    brightnesses, valid_map = framelet.get_pixel_val_at_surf_point(surface_raster)
    colors[...,2-col] += brightnesses
    color_counts[...,2-col] += valid_map

colors /= np.maximum(color_counts, 1)
colors *= 255 / np.max(colors)

colors = colors.astype(np.uint8)

new_img = Image.fromarray(colors)
new_img.save("./static/dep1.png")