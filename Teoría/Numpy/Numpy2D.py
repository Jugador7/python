# Import the libraries

import numpy as np

# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A

# Show the numpy array dimensions

A.ndim

# Show the numpy array shape

A.shape

# Show the numpy array size

A.size

# Access the element on the second row and third column

A[1, 2]

# Access the element on the second row and third column

A[1][2]

# Access the element on the first row and first column

A[0][0]

# Access the element on the first row and first and second columns

A[0][0:2]

# Access the element on the first and second rows and third column

A[0:2, 2]

# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y

Z = X + Y
Z

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2

Z = 2 * Y
Z

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y

# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X

# Multiply X with Y

Z = X * Y
Z

# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
A

# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
B

# Calculate the dot product

Z = np.dot(A,B)
Z

# Calculate the sine of Z

np.sin(Z)

# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C

C.T
