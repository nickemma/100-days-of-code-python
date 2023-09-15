# Question:
# def greet(name):
#     print(f"Hello, {name}!")

# greet("uoPeople") # Calling the function with an argument

# Explanation: The function greet() is defined with the parameter name. which is a placeholder for the value that will be passed the function is called with the argument "uoPeople".


# def greet(name):
#     print(f"Hello, {name}!")


# greet("uoPeople") # Call 1: Using a value as an argument


# person = "Nicholas" # Call 2: Using a variable as an argument
# greet(person)


# greet("Hello " + "Emmanuel") # Call 3: Using an expression as an argument

# Explanation: The function greet() is called three times and the value of the argument is assigned to the parameter name.

# def my_function():
#     my_variable = "Hello, world!"


# print(my_variable) # my_function()

# Explanation: The variable my_variable is defined inside the function my_function(). It's a local variable. It can only be accessed inside the function. When the function is called, the variable is created. When the function returns, the variable is destroyed. This means that my_variable is only accessible within the scope of my_function().


# print(f"Inside the function: parameter = {parameter}") # def unique_function(parameter):

# unique_function("Hello, world!")# Call the function

# print(f"Outside the function: parameter = {parameter}") # Try to use the parameter name outside the function

# Explanation: The variable parameter is defined inside the function unique_function(). we try to call it outside which results in a NameError because the parameter variable is undefined in the global scope. The parameter variable inside the function and the one outside the function are distinct and have separate scopes.


# name = "Global Name" # Global variable

# def my_function():

#     name = "Local Name" # Local variable with the same name as the global variable

#     print(f"Inside the function: name = {name}")


# my_function() # Call the function

# print(f"Outside the function: name = {name}")# Print the global variable

# Explanation: In summary, when a variable with the same name exists both globally and locally within a function, the local variable inside the function takes precedence within the function's scope. The global variable remains unaffected and retains its original value outside the function's scope.

# My Question # what is the difference between a function and a method?

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
def calculate_total_cost(item1_price, item2_price, item3_price):
    # Calculate the cost of individual items
    item1_cost = item1_price
    item2_cost = item2_price
    item3_cost = item3_price

    # Calculate the cost of combo packs with discounts
    combo1_cost = (item1_price + item2_price) * 0.9  # 10% discount
    combo2_cost = (item2_price + item3_price) * 0.9  # 10% discount
    combo3_cost = (item1_price + item3_price) * 0.9  # 10% discount
    combo4_cost = (item1_price + item2_price + item3_price) * \
        0.75  # 25% discount

    # Display the results
    print("Welcome to Amazon Store:")
    print("_______________________")
    print("\nproduct(s)  price")
    print(f"item 1        {item1_cost:.1f}")
    print(f"item 2        {item2_cost:.1f}")
    print(f"item 3        {item3_cost:.1f}")
    print(f"combo 1(item 1 + 2)   {combo1_cost:.1f}")
    print(f"combo 2(item 2 + 3)   {combo2_cost:.1f}")
    print(f"combo 3(item 1 + 3)   {combo3_cost:.1f}")
    print(f"combo 4(item 1 + 2 + 3)   {combo4_cost:.1f}")
    print("\nFor delivery contact:+192263568")


# Example usage:
item1_price = 200.0
item2_price = 400.0
item3_price = 600.0

calculate_total_cost(item1_price, item2_price, item3_price)

# Explanation: I defined a function calculate_total_cost that takes the prices of three different items (item1_price, item2_price, and item3_price) as arguments. Inside the function, I calculated the total cost of each individual item, which is simply the price of that item. Then, I calculated the cost of each combo by adding the prices of the items in the combo and subtracting 10% of the total cost of the combo. then calculate the cost of various combinations of items: combo1_cost: Combining item 1 and item 2, with a 10% discount applied combo2_cost: Combining item 2 and item 3, with a 10% discount applied combo3_cost: Combining item 1 and item 3, with a 10% discount applied combo4_cost: Combining all three items (gift pack), with a 25% discount applied. Finally, I displayed the results using the print() function. I called the function with the prices of three items as arguments.
