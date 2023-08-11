

import numpy as np

import matplotlib.pyplot as plt
fig, test = plt.subplots()
t = np.arange(0.0,5.0,0.001)
s = np.cos(3 *np.pi *t)
line = test.plot(t,s,lw=2)
test.annotate('Local Max', xy= (3.3,1),
              xytext=(3,1.8),arrowprops=dict(facecolor='green',shrink=0.05),)
test.set_ylim(-2,2)
plt.show()