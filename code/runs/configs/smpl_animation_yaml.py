
import yaml
import numpy as np


def smpl_anim_yaml_01(config_filename):
    anim_len = 90

    model_filename = '/body_reconstruction/smpl_animator/data/models/basicmodel_f_lbs_10_207_0_v1.1.0.pkl'

    joint = 19
    joint_rot_axis = np.array([0,1,0])
    joint_rot_angles = [0, np.pi/2.]

    betas = np.random.rand(300) * .03

    pose = np.random.rand(72) * .2
    pose[0] = np.pi
    pose[joint*3:joint*3+3] = joint_rot_axis * joint_rot_angles[0]

    poses = [pose.tolist()]

    for i in range(1, anim_len):
        pose = pose.copy()

        t = float(i)/anim_len
        pose[joint*3:joint*3+3] = joint_rot_axis * (t * (joint_rot_angles[1]-joint_rot_angles[0])+joint_rot_angles[0])

        poses.append(pose.tolist())

    cfg = {}
    cfg["SMPLModelFile"] = model_filename
    cfg["Betas"] = betas.tolist()
    cfg["Poses"] = poses

    stream = file(config_filename, 'w')
    yaml.dump(cfg, stream)
