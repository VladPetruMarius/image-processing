from skimage import io
import numpy as np
from matplotlib import pyplot as plt
import os.path

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images\\lena_color_256.tif")
my_image = io.imread(path)
print(my_image.min(), my_image.max())

my_image[10:200, 10:20, :] = [255, 255, 255]
plt.imshow(my_image)
plt.show()

