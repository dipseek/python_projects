import numpy as np
import matplotlib.pyplot as plt

width, height = 256, 256

random_data = np.random.rand(height, width)

plt.imshow(random_data, cmap='gray')
plt.axis('off') 
plt.savefig("random_image2.png", bbox_inches='tight', pad_inches=0)
plt.show()