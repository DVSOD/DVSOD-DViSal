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
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,
                                                     pinhole_camera_intrinsic
                                                     # o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault
                                                     )
# Flip it, otherwise the point cloud will be upside down.
pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])

# Visualize.
o3d.visualization.draw_geometries([pcd])