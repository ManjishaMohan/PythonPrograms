
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] =[7.00,3.50]
plt.rcParams["figure.autolayout"] = True
polygon1 = Polygon([(0,5),(1,1),(3,0),(4,6)])
x,y = polygon1.exterior.xy
plt.plot(x,y,c="red")
plt.show()
