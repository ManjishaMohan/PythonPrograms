
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.01, 10.0, 0.001)
data1 = np.exp(t)
data2 = np.cos(0.4 * np.pi * t)
fig, ax1 = plt.subplots()
color = 'tab:orange'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color = color)
ax1.plot(t, data1, color = color)
ax1.tick_params(axis ='y', labelcolor = color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('cos', color = color)
ax2.plot(t, data2, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
fig.suptitle('matplotlib.axes.Axes.twinx()function Example\n\n', fontweight ="bold")
plt.show()
