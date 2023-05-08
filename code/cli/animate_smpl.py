import sys

sys.path.append("./code/smpl/")
sys.path.append("./code/opendr_renderer/")

from smpl import SMPLAnimation
from opendr_animation import opendr_render_smpl_animation


def main_run_yaml(cfg):
    print("main run yaml")

    # load smpl parameters
    smpl_animation = SMPLAnimation(cfg["SMPLAnimationFile"])

    # OpenDR parameters
    opendr_params = cfg["OpenDRParameters"]

    # render animation frames
    frame_filename = cfg["FrameFilename"]
    opendr_render_smpl_animation(opendr_params, smpl_animation, frame_filename)

