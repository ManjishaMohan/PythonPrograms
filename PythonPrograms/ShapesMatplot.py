

import matplotlib.pyplot as plt
plt.axes()
circle = plt.Circle((0,0),radius=0.75,fc='r')
plt.gca().add_patch(circle)
plt.axis("scaled")
plt.show()