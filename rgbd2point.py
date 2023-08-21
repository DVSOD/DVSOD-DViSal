import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# Load data.
color_map = o3d.io.read_image("./data/color/00001.jpg")
depth_map = o3d.io.read_image("./data/depth/00001.png")
rgbd_image= o3d.geometry.RGBDImage.create_from_color_and_depth(color_map, depth_map)

plt.subplot(1, 2, 1)
plt.title('grayscale image')
plt.imshow(rgbd_image.color)
plt.subplot(1, 2, 2)
plt.title('depth image')
plt.imshow(rgbd_image.depth)
plt.show()

# The RGBD image can be converted into a point cloud, given a set of camera parameters.
# To be specific, some available camera intrinsic parameters are provided below:
'''
RGB-D People: http://www2.informatik.uni-freiburg.de/~spinello/RGBD-dataset.html
RGB-D Scene: https://rgbd-dataset.cs.washington.edu/dataset/rgbd-scenes-v2/
PTB: https://tracking.cs.princeton.edu/dataset.html
CDTB: Calibration parameters will be provided once requested
DET: Not provided. Because the main authors have left the university. (For reference purposes but not precise: https://www.intelrealsense.com/depth-camera-d415/)
Tracklam: http://tracklam.informatik.uni-freiburg.de/
Track3D: Not provided. But the authors directly provide the point cloud in https://github.com/yjybuaa/Track-it-in-3D. 
'''
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,
                                                     o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)

# Flip it, otherwise the point cloud will be upside down.
pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])

# Visualize.
o3d.visualization.draw_geometries([pcd])
