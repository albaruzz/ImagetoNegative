from matplotlib.image import imread
import matplotlib.pyplot as plt
import sys
  
img_bgr = imread(sys.path[0]+'\\lena.bmp')

fig = plt.figure(figsize=(10,7))
img1, img2 = fig.add_subplot(121), fig.add_subplot(122)
img1.imshow(img_bgr)

height, width, _ = img_bgr.shape
  
for i in range(0, height - 1):
    for j in range(0, width - 1):
          
        pixel = img_bgr[i, j]
          
        pixel[0] = 255 - pixel[0]
          
        pixel[1] = 255 - pixel[1]
          
        pixel[2] = 255 - pixel[2]
          
        img_bgr[i, j] = pixel
  
img2.imshow(img_bgr)

fig.show()
plt.show()