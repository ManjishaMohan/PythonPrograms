
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0] # explode is used to show particular part highlighted
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels ,startangle = 90,explode = myexplode, shadow = True,colors = mycolors) # to label the pie chart # startangle = 90
plt.legend(title = "Four Fruits:") #To add a list of explanation for each wedge, use the legend() function: # legends with header
plt.show()