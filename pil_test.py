from PIL import Image
"""
PIL的YUV通道分离与组合测试
"""

img_path = 'C:\\Users\\XueyanLiu\\Desktop\\文档\\lena.jpg'

img = Image.open(img_path)

y = img.convert('L')


img_yuv = img.convert('YCbCr')

_, u, v = img_yuv.split()

result = Image.merge('YCbCr', [y, u, v])

result_rgb = result.convert('RGB')
result_rgb.save('result.jpg')