
import yaml
import numpy as np
import click

import sys
sys.path.append("./code/runs/configs")

from smpl_animation_yaml import smpl_anim_yaml_01



def run_debug_01():
    w, h = (1250, 1250)

    cfg = {}

    # SMPL animation
    anim_filename = "/body_reconstruction/smpl_animator/data/animations/smpl_anim_01.yaml"
    smpl_anim_yaml_01(anim_filename)

    cfg["SMPLAnimationFile"] = anim_filename

    # OpenDR parameters
    cfg["OpenDRParameters"] = {}
    cfg["OpenDRParameters"]["Camera"] = {}

    cfg["OpenDRParameters"]["Camera"]["rt"] = np.zeros(3).tolist()
    cfg["OpenDRParameters"]["Camera"]["t"] = [0, 0, 1.5]
    cfg["OpenDRParameters"]["Camera"]["f"] = [w/2.,w/2.]
    cfg["OpenDRParameters"]["Camera"]["c"] = [w/2.,h/2.]
    cfg["OpenDRParameters"]["Camera"]["k"] = np.zeros(5).tolist()
    cfg["OpenDRParameters"]["Camera"]["near"] = 1.
    cfg["OpenDRParameters"]["Camera"]["far"] = 10.
    cfg["OpenDRParameters"]["Camera"]["width"] = w
    cfg["OpenDRParameters"]["Camera"]["height"] = h    

    cfg["OpenDRParameters"]["BGColor"] = np.zeros(3).tolist()

    lam_pt_light = {}
    lam_pt_light["light_type"] = "LambertianPointLight" 
    lam_pt_light["light_pos"] = [-1000,-1000,-2000]
    lam_pt_light["vc"] = [0.9, 0.9, 0.9]
    lam_pt_light["light_color"] = [1., 1., 1.]

    cfg["OpenDRParameters"]["Lights"] = [lam_pt_light]

    # Output frames
    cfg["FrameFilename"] = "/body_reconstruction/smpl_animator/data/videos/debug_01/frame_%07d.jpg"

    # Saving yaml
    stream = file("/body_reconstruction/smpl_animator/data/runs/run_debug_01.yaml", "w")
    yaml.dump(cfg, stream)



def main(run):
    if run == "run_debug_01":
        run_debug_01()



@click.command()
@click.option("--run", type=str, required=True)
def main_cmd(
    run
):
    main(
        run=run,
    )


if __name__ == "__main__":
    main_cmd()

