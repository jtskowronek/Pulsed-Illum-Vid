import matplotlib.pyplot as plt
import argparse
import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '1'
import numpy as np
from models import *
from functions.utils import *
import torch
import torch.optim
import torch.nn as nn

from skimage.measure import compare_psnr

torch.backends.cudnn.enabled = True
torch.backends.cudnn.benchmark =True
dtype = torch.cuda.FloatTensor



parser = argparse.ArgumentParser(description='Setting, compressive rate, size, and mode')

parser.add_argument('--iter', default=2000, type=int, help='max epoch')
parser.add_argument('--LR', default=0.01, type=float)
parser.add_argument('--frames', default=16, type=int, help='compressive rate')
parser.add_argument('--size', default=[256, 340], type=int, help='input image resolution')
parser.add_argument('--input', default='./input/', type=str, help='input path')
parser.add_argument('--output', default='./output/', type=str, help='output path')
parser.add_argument('--name', default='snapshot.tiff', type=str, help='input path')
parser.add_argument('--code', default=[1,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1], type=int, help='Code')
args = parser.parse_args()


if not os.path.exists(args.output):
        os.makedirs(args.output)


#Define Net
net = skip(input_depth, img_np.shape[0], 
               num_channels_down = [128] * 5,
               num_channels_up =   [128] * 5,
               num_channels_skip =    [128] * 5,  
               filter_size_up = 3, filter_size_down = 3, 
               upsample_mode='nearest', filter_skip_size=1,
               need_sigmoid=True, need_bias=True, pad=pad, act_fun='LeakyReLU').type(dtype)
net = net.cuda()
loss = nn.MSELoss()
loss.cuda()


gt,imgt = meas2tensor(args)
mask = code2tensor(args)





