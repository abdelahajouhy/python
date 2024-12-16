import numpy as np
import math
import matplotlib.pyplot as plt


x = np.random.rand(100)*(math.exp(100))
y = np.random.rand(100)
plt.scatter(x, y)
plt.title('Scatter Diagram')
plt.show()
