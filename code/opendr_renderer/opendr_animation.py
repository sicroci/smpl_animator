

from opendr.renderer import ColoredRenderer
from opendr.lighting import LambertianPointLight
from opendr.camera import ProjectPoints

import numpy as np

import cv2


def get_light(light, v, f):
    light_type = light["light_type"]

    if light_type == "LambertianPointLight":
        return LambertianPointLight(
            f=f,
            v=v,
            num_verts=len(v),
            light_pos=np.array(light["light_pos"]),
            vc=np.multiply(np.ones_like(v), light["vc"]),
            light_color=np.array(light["light_color"])
        )


def opendr_render_smpl_animation(opendr_params, smpl_animation, frame_filename):
    w = opendr_params["Camera"]["width"]
    h = opendr_params["Camera"]["height"]
    rt = np.array(opendr_params["Camera"]["rt"])
    t = np.array(opendr_params["Camera"]["t"])
    f = np.array(opendr_params["Camera"]["f"])
    c = np.array(opendr_params["Camera"]["c"])
    k = np.array(opendr_params["Camera"]["k"])
    near = opendr_params["Camera"]["near"] 
    far = opendr_params["Camera"]["far"]
    bgcolor = np.array(opendr_params["BGColor"])
    lights = opendr_params["Lights"]
    
    # Create OpenDR renderer
    rn = ColoredRenderer()

    #
    frame_num = smpl_animation.get_frame_num()

    for frame_i in range(frame_num):
        print("Rendering frame: " + str(frame_i+1) + " / " + str(frame_num))

        m = smpl_animation.get_smpl_model(frame_i)

        # Assign attributes to renderer
        rn.camera = ProjectPoints(v=m, rt=rt, t=t, f=f, c=c, k=k)
        rn.frustum = {'near': near, 'far': far, 'width': w, 'height': h}
        rn.set(v=m, f=m.f, bgcolor=bgcolor)

        # Construct light sources
        assert len(lights) == 1 # TODO Extend code to multiple light sources
        rn.vc = get_light(lights[0], m, m.f)

        # Render frame
        frame = rn.r*255

        # Save frame
        cv2.imwrite(frame_filename % frame_i, frame)

