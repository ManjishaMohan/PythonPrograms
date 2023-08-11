
'''
Write a NumPy program to create an array of the integers from 30 to 70.
Write a NumPy program to get the numpy version and show numpy build configuration
Write a NumPy program to test whether none of the elements of a given array is zero
Write a NumPy program to test whether any of the elements of a given array is non-zero
Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives

--------------------------------------------------------------
10 minutes -:11:45 am
'''
#Write a NumPy program to create an array of the integers from 30 to 70.
import numpy as np
arr=np.arange(30,70)
print("integer from 30 to 70 :-", arr)
#Write a NumPy program to get the numpy version and show numpy build configuration
import numpy as np
print(np.__version__)
print(np.__config__)

#Write a NumPy program to test whether none of the elements of a given array is zero
import numpy as np
arr=np.array([5,6,0,8])
print("array :-",arr)
print(np.all(arr))
#Write a NumPy program to test whether any of the elements of a given array is non-zero
import numpy as np
arr=np.array([5,6,0,8])
print("array :-",arr)
print(np.any(arr))
#Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives
import numpy as np
arr=np.zeros(10)
print("zeros",arr)
arr=np.ones(10)
print("ones",arr)
arr=np.ones(10)*5
print("fives",arr)