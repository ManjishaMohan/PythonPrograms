

#Write a NumPy program to get the numpy version and show numpy build configuration.

import numpy as np
print(np.__version__)
print(np.show_config())
#Write a NumPy program to swap rows and columns of a given array in reverse order
import numpy as np
nums = np.array([[[1, 2, 3, 4],
               [0, 1, 3, 4],
               [90, 91, 93, 94],
               [5, 0, 3, 2]]])
print("Original array:")
print(nums)
print("\nSwap rows and columns of thearray in reverse order:")
new_nums = print(nums[::-1, ::-1])
print(new_nums)
#Write a NumPy program to create a three-dimension array with shape (3,5,4) and set to a variable
import numpy as np

nums = np.array([[[1, 5, 2, 1],
                  [4, 3, 5, 6],
                  [6, 3, 0, 6],
                  [7, 3, 5, 0],
                  [2, 3, 3, 5]],

                 [[2, 2, 3, 1],
                  [4, 0, 0, 5],
                  [6, 3, 2, 1],
                  [5, 1, 0, 0],
                  [0, 1, 9, 1]],

                 [[3, 1, 4, 2],
                  [4, 1, 6, 0],
                  [1, 2, 0, 6],
                  [8, 3, 4, 0],
                  [2, 0, 2, 8]]])
print("Array:")
print(nums)

#Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number

import numpy as np
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.32, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
n = 8.32
r = 18.32
print("\nReplace elements of the said array which are equal to ",n,"with",r)
print(np.where(nums == n, r, nums))
print("\nReplace elements with of the said array which are less than",n,"with",r)
print(np.where(nums < n, r, nums))
print("\nReplace elements with of the said array which are greater than",n,"with",r)
print(np.where(nums > n, r, nums))

#Write a NumPy program to create an array of equal shape and data type of a given array
import numpy as np
nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.32, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
print("\nNew array of equal shape and data type of the said array filled by 0:")
print(np.zeros_like(nums))