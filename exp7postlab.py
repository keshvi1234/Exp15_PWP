# a.	Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


# b.	Write a NumPy program to reverse an array (the first element becomes the last).
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)


# c.	Write a NumPy program to find common values between two arrays.
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
common_values = np.intersect1d(arr1, arr2)
print(common_values)



# d.	Write a NumPy program to repeat array elements.
import numpy as np
arr = np.array([1, 2, 3])
repeated_arr = np.repeat(arr, 3)
print(repeated_arr)



# e.	Write a NumPy program to find the memory size of a NumPy array.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Memory size of the array:", arr.nbytes, "bytes")



# f.	Write a NumPy program to create an array of ones and zeros.
import numpy as np
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((3, 3))
print("Array of Zeros:\n", zeros_arr)
print("Array of Ones:\n", ones_arr)



# g.	Write a NumPy program to find the 4th element of a specified array.
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
fourth_element = arr[3]   # index starts from 0
print("The 4th element is:", fourth_element)
