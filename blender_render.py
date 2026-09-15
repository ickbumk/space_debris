import blenderproc as bproc
import numpy as np
import imageio.v2 as imageio
import bpy

# Initialize BlenderProc
bproc.init()

# Load object
obj_path = "/home/asclab/projects/NBV/datasets/gso/Schleich_Bald_Eagle/meshes/model.obj"
objs = bproc.loader.load_obj(obj_path)
obj = objs[0]
obj.set_location([0.0, 0.0, 0.0])

# Load all rotations
rotations = np.loadtxt("rotations.txt")

# Camera
cam_location = np.array([0.8, -0.8, 0.8])
poi = np.array([0.0, 0.0, 0.0])

rotation_matrix = bproc.camera.rotation_from_forward_vec(
    poi - cam_location
)

cam2world = bproc.math.build_transformation_mat(
    cam_location,
    rotation_matrix
)

bproc.camera.add_camera_pose(cam2world)
bproc.camera.set_resolution(1800, 1600)

K = bproc.camera.get_intrinsics_as_K_matrix()
print(K)

# Light
light = bproc.types.Light()
light.set_type("POINT")
light.set_location([5, 5, 5])
light.set_energy(1000)

# Output directory
output_dir = "/home/asclab/projects/NBV/rlnbvp/render_output"

# Enable depth output
bproc.renderer.enable_depth_output(activate_antialiasing=False)

# Render
for i, euler in enumerate(rotations[:3]):

    obj.set_rotation_euler(euler)

    data = bproc.renderer.render()

    rgb = data["colors"][0]
    depth = data["depth"][0]

    # Save RGB
    imageio.imwrite(
        f"{output_dir}/rgb_{i:04d}.png",
        rgb
    )

    # Save depth (recommended: float32)
    np.save(
        f"{output_dir}/depth_{i:04d}.npy",
        depth.astype(np.float32)
    )

    print(f"Saved frame {i}")

# Save scene
bpy.ops.wm.save_as_mainfile(
    filepath=f"{output_dir}/scene.blend"
)