def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b
result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12

string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])   # Output: 5

total = sum([10, 20, 30, 40, 50])  # Output: 150

highest = max([5, 12, 8, 23, 16])  # Output: 23

lowest = min([5, 12, 8, 23, 16])  # Output: 5

def function_name():
    pass

def greet(name):
    print("Hello, " + name)
result = greet("Alice")
print(result)  # Output: Hello, Alice

def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)

def add(a, b):
    return a + b
sum_result = add(3, 5)  # sum_result gets the value 8

global_variable = "I'm global

def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

example_function()

print(global_variable) 

#print(local_variable)  # Error, local variable not visible here

def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)  # Output: 1 2 3 4 5

def greet(name):
    return "Hello, " + name
for _ in range(3):
    print(greet("Alice"))

# Define an empty list as the initial data structure
my_list = []

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

print("Current list:", my_list)

# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list

# Print the updated list
print("Updated list:", my_list)
