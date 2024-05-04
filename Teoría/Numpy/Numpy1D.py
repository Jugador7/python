pip install numpy

# import numpy library

import numpy as np 

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)

# Check the type of the array

type(a)

# Check the type of the values stored in numpy array

a.dtype

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c


# Assign the first element to 100

c[0] = 100
c

# Assign the 5th element to 0

c[4] = 0
c

# Slicing the numpy array

d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c

#We can also define the steps in slicing, like this: [start:end:step].

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#If we don't pass start its considered 0
print(arr[:4])

#If we don't pass end it considers till the length of array.

print(arr[4:])

#If we don't pass step its considered 1

print(arr[1:5:])

# Create the index list

select = [0, 2, 3, 4]
select

# Use List to select elements

d = c[select]
d

# Assign the specified elements to new value

c[select] = 100000
c

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array

a.size

# Get the number of dimensions of numpy array

a.ndim

# Get the shape/size of numpy array

a.shape

### Numpy Statistical Functions

# Create a numpy array

a = np.array([1, -1, 1, -1])

# Get the mean of numpy array

mean = a.mean()
mean

# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array

max_b = b.max()
max_b

# Get the smallest value in the numpy array

min_b = b.min()
min_b

## Numpy Array Operations

### Array Addition
u = np.array([1, 0])
u

v = np.array([0, 1])
v

# Numpy Array Addition

z = np.add(u, v)
z

# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

  # Plot numpy arrays

Plotvec1(u, z, v)

### Adding Constant to a Numpy Array

# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u

# Add the constant to array

u + 1

# The value of pi

np.pi

# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)
y

## Linspace

# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)

# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)
x

# Calculate the sine of x list

y = np.sin(x)

# Plot the result

plt.plot(x, y)

### Iterating 1-D Arrays

arr1 = np.array([1, 2, 3])
print(arr1)

#But if you want to result in the form of the list, then you can use for loop:
for x in arr1:
  print(x)

# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Write your code below and press Shift+Enter to execute
a = np.array([-1,1])
a
b = np.array([1,1])
b

Plotvec2(a, b)

print("El producto es: ", np.dot(a,b))

