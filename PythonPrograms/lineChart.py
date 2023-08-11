
import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([0, 20, 40, 60, 80, 100])

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Draw a line")
plt.grid(True)
plt.show()
