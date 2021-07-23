import matplotlib.pyplot as plt
from pylab import *

x = arange(0.0, 1.0, 0.01)
y = sin(2*pi*x)

plt.plot(x, y)
plt.show()
