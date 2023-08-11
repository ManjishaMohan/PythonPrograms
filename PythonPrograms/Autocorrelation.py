

import matplotlib.pyplot as plt
import numpy as np

data = np.array([12.0,24.0,7.,20.0,
                 7.0,22.0,18.0,22.0,
                 6.0,7.0,20.0,13.0,
                 8.0,5.0,8])
plt.title("Autocorrelation Plot")
#Providing x axis name
plt.xlabel("LAGS")
#plotting the autocorrelaton plot
plt.acorr(data, maxlags = 10)
# Display the plot
print("The Autocorrelation plot for data is: ")
plt.grid(True)
plt.show()
