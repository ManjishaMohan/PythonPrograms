
import matplotlib.pyplot as plt

x = ['Mon','Tues','wed','Thurs','Fri']
y1 = [1,2,5,8,9]
y2 = [10,11,10,10,10]

plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')
plt.grid(True)
plt.show()

