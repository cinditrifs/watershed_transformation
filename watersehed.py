import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    imgray = np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
    return imgray

file = 'images.png'
img = mpimg.imread(file)
gray = rgb2gray(img)

##convert grayscale image to list pixel 
newimage = gray
matriks = np.array(newimage)
pixel = matriks.tolist ()


plt.imshow(gray, cmap = plt.get_cmap('gray'))
imagenew = ('images_greyscale.png')
plt.savefig(imagenew)
plt.show()
print (pixel)
