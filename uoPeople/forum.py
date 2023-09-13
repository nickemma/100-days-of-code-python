# Question:
# def greet(name):
#     print(f"Hello, {name}!")


# Calling the function with an argument
# greet("uoPeople")
# Explanation: The function greet() is defined with the parameter name. It's a placeholder for the value that will be passed when the function is called. When the function is called with the argument "uoPeople", the value of the argument is assigned to the parameter name. The function then prints "Hello, uoPeople!".


# def greet(name):
#     print(f"Hello, {name}!")


# Call 1: Using a value as an argument
# greet("uoPeople")

# Call 2: Using a variable as an argument
# person = "Nicholas"
# greet(person)

# Call 3: Using an expression as an argument
# greet("Hello " + "Emmanuel")

# Explanation: The function greet() is called three times. The first call passes the value "uoPeople" as an argument. The second call passes the value of the variable person as an argument. The third call passes the value of the expression "Hello " + "Emmanuel" as an argument. In all three cases, the value of the argument is assigned to the parameter name.

# def my_function():
#     my_variable = "Hello, world!"


# my_function()
# print(my_variable)
# Output: NameError: name 'my_variable' is not defined
# Explanation: The variable my_variable is defined inside the function my_function(). It's a local variable. It can only be accessed inside the function. When the function is called, the variable is created. When the function returns, the variable is destroyed. This means that my_variable is only accessible within the scope of my_function().

# def unique_function(parameter):
#     print(f"Inside the function: parameter = {parameter}")


# Call the function
# unique_function("Hello, world!")

# Try to use the parameter name outside the function
# print(f"Outside the function: parameter = {parameter}")
# Output: NameError: name 'parameter' is not defined
# Explanation: The variable parameter is defined inside the function unique_function(). It's a function's local scope. After calling the function, we attempt to print the value of parameter outside the function. However, this results in a NameError because the parameter variable is undefined in the global scope. The parameter variable inside the function and the one outside the function are distinct and have separate scopes.

# Global variable
# name = "Global Name"


# def my_function():
# Local variable with the same name as the global variable
# name = "Local Name"

# Print the local variable
# print(f"Inside the function: name = {name}")


# Call the function
# my_function()

# Print the global variable
# print(f"Outside the function: name = {name}")

# Output: Inside the function: name = Local Name and Outside the function: name = Global Name
# Explanation: The variable name is defined in the global scope and also a function is defined. Inside the function, the defined local variable name with the value "Local Name", which (takes precedence over) the global variable with the same name within the function's scope. Inside the function: name = Local Name" because the local variable is accessed within the function's scope. After calling the function,     we attempt to print the global variable name outside the function. It prints "Outside the function: name = Global Name" because we are now accessing the global variable, not the local one.

# In summary, when a variable with the same name exists both globally and locally within a function, the local variable inside the function takes precedence within the function's scope. The global variable remains unaffected and retains its original value outside the function's scope.

# what question can i ask my instructor about this topic?
# what is the difference between a function and a method?

# Programming assignment 1

# import math


# def print_circum(radius):
#     circumference = 2 * math.pi * radius
#     print(
#         f"The circumference of the circle with radius {radius} is approximately {circumference:.5f}")


# Call 1: Radius = 5.0
# print_circum(5.0)
# Output: The circumference of the circle with radius 5.0 is approximately 31.41593

# Call 2: Radius = 7.5
# print_circum(7.5)
# Output: The circumference of the circle with radius 7.5 is approximately 47.12389

# Call 3: Radius = 3.14159
# print_circum(3.14159)
# Output: The circumference of the circle with radius 3.14159 is approximately 19.73921


# Programming assignment 2
# def calculate_total_cost(item1_price, item2_price, item3_price):
#     # Calculate the cost of individual items
#     item1_cost = item1_price
#     item2_cost = item2_price
#     item3_cost = item3_price

#     # Calculate the cost of combo packs with discounts
#     combo1_cost = (item1_price + item2_price) * 0.9  # 10% discount
#     combo2_cost = (item2_price + item3_price) * 0.9  # 10% discount
#     combo3_cost = (item1_price + item3_price) * 0.9  # 10% discount
#     combo4_cost = (item1_price + item2_price + item3_price) * \
#         0.75  # 25% discount

#     # Display the results
#     print("Welcome to Amazon Store:")
#     print("_______________________")
#     print("\nproduct(s)  price")
#     print(f"item 1        {item1_cost:.1f}")
#     print(f"item 2        {item2_cost:.1f}")
#     print(f"item 3        {item3_cost:.1f}")
#     print(f"combo 1(item 1 + 2)   {combo1_cost:.1f}")
#     print(f"combo 2(item 2 + 3)   {combo2_cost:.1f}")
#     print(f"combo 3(item 1 + 3)   {combo3_cost:.1f}")
#     print(f"combo 4(item 1 + 2 + 3)   {combo4_cost:.1f}")
#     print("\nFor delivery contact:+192263568")


# Example usage:
# item1_price = 200.0
# item2_price = 400.0
# item3_price = 600.0

# calculate_total_cost(item1_price, item2_price, item3_price)

# Explanation: I defined a function calculate_total_cost that takes the prices of three different items (item1_price, item2_price, and item3_price) as arguments. Inside the function, I calculated the total cost of each individual item, which is simply the price of that item. Then, I calculated the cost of each combo by adding the prices of the items in the combo and subtracting 10% of the total cost of the combo. then calculate the cost of various combinations of items: combo1_cost: Combining item 1 and item 2, with a 10% discount applied combo2_cost: Combining item 2 and item 3, with a 10% discount applied combo3_cost: Combining item 1 and item 3, with a 10% discount applied combo4_cost: Combining all three items (gift pack), with a 25% discount applied. Finally, I displayed the results using the print() function. I called the function with the prices of three items as arguments.
