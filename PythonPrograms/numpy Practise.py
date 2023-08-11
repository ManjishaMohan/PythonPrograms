
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0]) #indexing
print(arr[1:4]) #slicing
print(arr)
print(type(arr)) #type

#join
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)