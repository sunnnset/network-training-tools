import os
txt_dir = 'F:\\LightField-SR\\512-patch-gauss\\test_list.txt'
lines  = open(txt_dir,'r') 
txt_list = []
for line in lines:
    txt_list.append(line[:-1])
lines.close()
print(len(txt_list))
for item in txt_list:
    print(item)
