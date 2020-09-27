from PIL import Image
import os
import cv2
import numpy as np
from albumentations import ShiftScaleRotate, RandomCrop, HorizontalFlip, VerticalFlip, Compose, CenterCrop, HueSaturationValue
# import ipdb
import torch
import numpy as np
"""
使用albumentations进行数据增强（超分辨数据集）
"""


base = 'F:\\LightField-SR\\'
folder_dir = base+'工业相机-标定板数据集\\'
target_img_dir = base + 'crop\\'

aug = Compose([
        CenterCrop(height=4500, width=4500, p=1),
        RandomCrop(height=512, width=512, p=1),
        VerticalFlip(),
        HorizontalFlip(),
        HueSaturationValue(p=0.5, hue_shift_limit=(-20, 20), sat_shift_limit=(-30, 30), val_shift_limit=(-20, 20))
                         ])

folder_list = os.listdir(folder_dir)
length = str(27*14*8)
ii = 0
for folder in folder_list:
    img_dir = folder_dir+folder+'\\'
    img_list = os.listdir(img_dir)

    for file in img_list:
        
        img = Image.open(img_dir+file)
        img = np.array(img)
        for i in range(8):
            print(str(ii)+'/'+length)
            while True:
                augmented = aug(image=img)['image']
                img_save = Image.fromarray(augmented)
                avg = np.average(augmented)
                max = np.max(np.max(augmented))
                if avg > 15 and max >100:
                    break
            # print(str(i)+' '+str(avg))
            # augmented = aug(image=img)['image']
            # img_save = Image.fromarray(augmented)
            file_name = str(folder)+'_'+file[:-4]
            postfix = '_'+str(i)+'.jpg'
            img_save.save(target_img_dir+file_name+postfix)
            ii += 1
