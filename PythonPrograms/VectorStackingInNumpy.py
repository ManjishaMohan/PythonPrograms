
import numpy as np

in_arr1 = np.array([1,2,3])
print("first array : \n ", in_arr1)

in_arr2 = np.array([4,5,6])
print("first array : \n ", in_arr2)

#stacking the array with axis = 0
out_arr1 = np.stack((in_arr1,in_arr2),axis=0)
print("output of stacked arrays with 0 axis:\n",out_arr1)

#stacking the array with axis = 1
out_arr2 = np.stack((in_arr1,in_arr2),axis=1)
print("output of stacked arrays with 1 axis:\n",out_arr2)