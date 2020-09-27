import os
import shutil
import random
"""
将光场图像随机分割为训练集和测试集
"""


mylist = []
for i in range(170,310,10):
    for j in range(1,28):
        prefix = str(i)+'_'+str(j)
        # print(prefix)
        mylist.append(prefix)
random.shuffle(mylist)
for item in mylist:
    print(item)
trainset_size = int(len(mylist)/5*4)
train_list = mylist[:trainset_size]
test_list = mylist[trainset_size:]
print(len(train_list),len(test_list))

base_dir = 'F:\\LightField-SR\\512-patch-gauss\\target\\'
test_dir = 'F:\\LightField-SR\\512-patch-gauss\\target_test\\'
for prefix in test_list:
    for i in range(8):
        file_name = prefix + '_' + str(i) + '.jpg'
        print(file_name)
        shutil.move(base_dir+file_name, test_dir+file_name)
