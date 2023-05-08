
import yaml
import numpy as np

from smpl_webuser.serialization import load_model


class SMPL:
    def __init__(self, model, betas, pose):
        self.set_parameters(model, betas, pose)

    def set_parameters(self, model, betas, pose):
        self.model = model
        self.betas = betas
        self.pose = pose
    
    def load_model(self):
        self.model.betas[:] = self.betas        
        self.model.pose[:] = self.pose

    def get_model(self):
        self.load_model()
        return self.model
    


class SMPLAnimation:
    def __init__(self, config_filename):
        self.load_models_from_yaml(config_filename)

    def load_models_from_yaml(self, config_filename):
        stream = file(config_filename, 'r')
        cfg = yaml.safe_load(stream)

        # load template model
        model = load_model(cfg["SMPLModelFile"])

        # load shape parameters
        betas = np.array(cfg["Betas"])

        # load pose parameters
        self.models = []
        for pose in cfg["Poses"]:
            self.models.append(SMPL(model, betas, np.array(pose)))

    def get_smpl_model(self, frame_i):
        return self.models[frame_i].get_model()
    
    def get_frame_num(self):
        return len(self.models)
