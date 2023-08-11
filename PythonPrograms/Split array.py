

# Split of array into elements
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
# split of array into array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0]) # indexing
print(newarr[1])
print(newarr[2])
#splitting 2D array

import numpy as np
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr=np.array_split(arr,3)
print(newarr)