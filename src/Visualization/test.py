import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y, label='y = x^2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y = x^2')


plt.legend()

plt.show()
