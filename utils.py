from PIL import Image
import matplotlib.pyplot as plt

import time,os

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

def is_file_allow(filename):

    '''Function for checking image in right extension'''

    # check whether . present in name or not
    if not "." in filename:
        return False

    # get last string after . (basically to get extension)
    suffix=filename.rsplit('.',1)[1]

    # check if file is in jpef, png, jpg
    if suffix.lower in ['jpeg','png','jpg']:
        return True
    else:
        return False
        

def image_loader(img_path,Loader,device):
    img = Image.open(img_path)

    if img_path[-3:].lower() == 'png':
        img = img.convert('RGB')
    
    img = loader(img).unsqueeze(0)

    return img.to(device,torch.float)

def get_input_optimizer(input_img):
    optimizer = optim.LBFGS([input_img, requires_grad_()])

def add_time(filename):
    img_name = filename.rsplit('.')[0]
    img_suffix = filename.rsplit('.')[1]

    filename = str(time.time()).replace('.','_') + '.' + img_suffix
    return filename

def imshow(tensor, loader, unloader, title=None, output=False, folder=''):

    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)

    plt.imshow(image)

    if title is not None:
        plt.title(title)
    if output:
        output_name = 'result' + '?' + str(time.time()) + '.png'
        plt.savefig(
            folder + '/' + output_name, 
            bbox_inches=None,
            pad_inches=0.)
        plt.close()
        return output_name