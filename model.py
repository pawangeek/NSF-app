import torch
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

from utils import image_loader,imshow

def run_model(style, content, folder):

    device = torch.device("cuda" if torch.cuda.is_available else "cpu")

    if torch.cuda.is_available:
        imsize=(512,512)

    else:
        imsize=(128,128)

    trans = [transforms.Resize(imsize), transforms.ToTensor()]
    loader = transforms.Compose(trans)

    style_img = image_loader(folder + '/' + content, loader, device)
    content_img = image_loader(folder + '/' + style, loader, device)

    unloader = transforms.ToPILImage()

    cnn = models.vgg19(pretrained=True).features.to(device).eval()

    vgg_mean = torch.tensor([0.485,0.456,0.406])
    vgg_std = torch.tensor([0.229,0.224,0.225])

    input_img = content_img.clone()

    output = run_style_transfer(cnn, vgg_mean, vgg_std, content_img, style_img, input_img, device, loader, unloader, folder)


    plt.figure(figsize=(8,8))

    output_name = imshow(output,loader, unloader,folder,output=True,title='output image')

    return output_name

