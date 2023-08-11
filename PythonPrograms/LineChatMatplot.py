
from matplotlib import pyplot as plt
#x axis value
x=[1,2,9,4,7]

#y axis value
y=[10,5,8,4,2]

plt.plot(x,y) #function to plot
plt.xlabel("year")
plt.ylabel("time")
plt.title("trend")
plt.show()  #function to show the plot


x=[2000,2001,2002,2004]
y=[2,4,8,10]
plt.plot(x,y)
plt.xlabel("year")
plt.ylabel("target")
plt.title("sales graph")
plt.show()