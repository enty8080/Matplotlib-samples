import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, num=100)
y = np.exp(x)

plt.plot(x, y)
plt.title('Exponential Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
