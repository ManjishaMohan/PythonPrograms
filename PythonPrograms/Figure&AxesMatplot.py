
import matplotlib.pyplot as plt

y=[1,4,9,16,25,36,49,64]
x1=[1,16,30,42,55,68,77,88]
x2=[1,6,12,18,28,40,52,65]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(x1,y,'ys-') # Solid line with yelow color and square marker
l2 = ax.plot(x2,y,'go--') # dash line with green color and circle marker
ax.legend(labels = ('tv','smartphone'),loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effects on sales")
ax.set_xlabel("Medium")
ax.set_ylabel("Sales")
plt.show()
