import torch
from PIL import Image
import numpy as np




def meas2tensor(params):
     fullpath = params.input+params.name
     im = Image.open(fullpath)
     input = np.array(im)
     input = torch.from_numpy(input)
     input = torch.unsqueeze(input,0)
     input = torch.unsqueeze(input,0)
     input = input.cuda().float()
     return input,im

def code2tensor(params):

    code = np.array(params.code)
    code = torch.from_numpy(code)

    mask = torch.ones(size=(params.size[0],params.size[1],params.frames))
    mask = mask*code
    mask = torch.permute(mask,(2,0,1))
    mask = torch.unsqueeze(mask,0).cuda().float()
    return(mask)



def torch_to_np(img_var):
    '''Converts an image in torch.Tensor format to np.array.
    From 1 x C x W x H [0..1] to  C x W x H [0..1]
    '''
    return img_var.detach().cpu().numpy()[0]    