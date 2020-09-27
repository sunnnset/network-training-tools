import os
import shutil

DATA_X_PATH = "F:\\LightField-SR\\512-patch\\input\\"

output_base = 'F:\\LightField-SR\\512-patch\\'
network_output = output_base+'network-output\\'
train_output = output_base+'train-output\\'
test_output = output_base+'test-output\\'
os.makedirs(train_output, exist_ok=True)
os.makedirs(test_output, exist_ok=True)


TRAIN_TEST_RATIO = (8, 2)  # sum should be 10

def get_image_list(data_path):
    l = os.listdir(data_path)
    train_list = []
    for f in l:
        if f[-4:] == '.png' or f[-4:] == '.jpg':
            train_list.append(f)
    return train_list

img_list = get_image_list(DATA_X_PATH)
imgs_to_train = len(img_list) * TRAIN_TEST_RATIO[0] // 10
train_list = img_list[:imgs_to_train]
test_list = img_list[imgs_to_train:]


for file in train_list:
    print(file)
    shutil.move(network_output+file, train_output+file)
for file in test_list:
    print(file)
    shutil.move(network_output+file, test_output+file)

