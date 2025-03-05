import numpy as np
import matplotlib.pylab as plt
import step

x = np.arange(-5, 5, .1)
y = step.step_function(x)
plt.plot(x, y)
plt.ylim(-.1, 1.1)
plt.show()

