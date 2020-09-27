from PIL import Image
import numpy as np
import os
import shutil
"""
删除patch中接近全黑的无效图像
"""


hr_dir = 'F:\\LightField-SR\\512-patch\\target\\'
too_black_dir = 'F:\\LightField-SR\\512-patch\\too_black\\'

file_list = os.listdir(hr_dir)
count = 0
for file in file_list:
    img = Image.open(hr_dir+file)
    img_array = np.array(img)
    avg = np.average(img_array)
    if avg < 15:
        print(file+' '+str(avg))
        count += 1
        shutil.move(hr_dir+file, too_black_dir+file)
print('count: '+str(count))
    
    # resize.save(lr_dir+file)