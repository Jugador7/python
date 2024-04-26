#ZERO ERROR
result = 10 / 0 
print(result)
# Raises ZeroDivisionError

# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")

#VALUE ERRROR
num = int("abc")
# Raises ValueError

#FILE NOT FOUND
with open("nonexistent_file.txt", "r") as file:
        content = file.read()   # Raises FileNotFoundError

#INDEX ERROR
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError

#
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError

#
result = "hello" + 5   
# Raises TypeError

#
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError

#This error is encountered when an attempt is made to import a module that is unavailable. For example: import non_existent_module
