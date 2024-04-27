
class ClassName:

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        pass
        # ...

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ...):
        # Method logic
        pass

  
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ...):
        # Method logic
        pass
    def method2(self, parameter1, parameter2, ...):
        # Method logic
        pass

  # Create objects (instances) of the class
object1 = ClassName(arg1, arg2, ...)
object2 = ClassName(arg1, arg2, ...)

# Calling methods on objects
# Method 1: Using dot notation
result1 = object1.method1(param1_value, param2_value, ...)
result2 = object2.method2(param1_value, param2_value, ...)

# Calling methods on objects
# Method 1: Using dot notation
result1 = object1.method1(param1_value, param2_value, ...)
result2 = object2.method2(param1_value, param2_value, ...)

# Method 2: Assigning object methods to variables
method_reference = object1.method1  # Assign the method to a variable
result3 = method_reference(param1_value, param2_value, ...)

# Accessing object attributes
attribute_value = object1.attribute1  # Access the attribute using dot notation

# Modifying object attributes
object1.attribute2 = new_value  # Change the value of an attribute using dot notation

# Accessing class attributes (shared by all instances)
class_attr_value = ClassName.class_attribute

#Método para mostrar propiedades de un objeto. 
    def show_properties(self):
        print("Properties of the Vehicle:")
        print(self.maximum_speed)
        print(self.mileage)
        print(self.seats)

Example:

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
