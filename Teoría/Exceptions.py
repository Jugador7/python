#ZERO ERROR
result = 10 / 0 
print(result)
# Raises ZeroDivisionError

a = 1

# using Try- except 
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        
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


#TRY EXCEPT ESCPECIFIC
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

#TRY EXCEPT ELSE AND FINALLY

# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)

#GREAT EXAMPLE
def safe_divide(numerator,denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")
    else:
        print("success result=",result)
    finally:
        print("Processing Complete")
        
    
numerator = int(input("Please enter a number to divide from"))
denominator = int(input("Please enter a number to divide by"))
print(safe_divide(numerator,denominator)) 
