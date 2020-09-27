from PIL import Image, ImageFilter
import numpy as np
import os
"""
对高分辨率图片进行高斯滤波，并插值到1/2尺寸
"""


hr_dir = 'F:\\LightField-SR\\512-patch-gauss\\target\\train\\'
lr_dir = 'F:\\LightField-SR\\512-patch-gauss\\input_r1.7\\train\\'

file_list = os.listdir(hr_dir)
for file in file_list:
    print(file)
    img = Image.open(hr_dir+file)
    img = img.filter(ImageFilter.GaussianBlur(radius=1.7))
    resize = img.resize((256,256), Image.BICUBIC)
    resize.save(lr_dir+file)
