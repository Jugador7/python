# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
'hard rock'.split()

# Split the string by comma
'A,B,C,D'.split(',')

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Clone (clone by value) the list A

B = A[:]
B
