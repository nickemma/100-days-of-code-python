# # Programming assignment 1

# import math


# def print_circum(radius):
#     # Define a custom message based on the radius
#     if radius < 1:
#         message = "That's a tiny circle!"
#     elif radius > 10:
#         message = "Wow, that's a big circle!"
#     else:
#         message = "A standard-sized circle."

#     circumference = 2 * math.pi * radius

#     # Add some creativity to the output message
#     print(
#         f"{message} The circumference of the circle with radius {radius} is approximately {circumference:.5f}.")


# # Call 1: Radius = 5.0
# print_circum(5.0)
# output = "A standard-sized circle. The circumference of the circle with radius 5.0 is approximately 31.41593."

# # Call 2: Radius = 7.5
# print_circum(7.5)


# # Call 3: Radius = 3.14159
# print_circum(3.14159)


# # Explanation: I defined a function print_circum that takes the radius of a circle as an argument. Inside the function, I calculated the circumference of the circle using the formula 2πr, where r is the radius of the circle. Then, I displayed the result using the print() function. I called the function with three different values of radius: 5.0, 7.5, and 3.14159. The output of the program is shown below.


# # Programming assignment 2
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


# # Example usage:
# item1_price = 200.0
# item2_price = 400.0
# item3_price = 600.0

# calculate_total_cost(item1_price, item2_price, item3_price)

# # Explanation: I defined a function calculate_total_cost that takes the prices of three different items (item1_price, item2_price, and item3_price) as arguments. Inside the function, I calculated the total cost of each individual item, which is simply the price of that item. Then, I calculated the cost of each combo by adding the prices of the items in the combo and subtracting 10% of the total cost of the combo. then calculate the cost of various combinations of items: combo1_cost: Combining item 1 and item 2, with a 10% discount applied combo2_cost: Combining item 2 and item 3, with a 10% discount applied combo3_cost: Combining item 1 and item 3, with a 10% discount applied combo4_cost: Combining all three items (gift pack), with a 25% discount applied. Finally, I displayed the results using the print() function. I called the function with the prices of three items as arguments.

# # create an expression


# def greet(name):
#     print(f"Hello, {name}!")
#     print("Welcome to UoPeople")


# greet("John")
# greet("Mary")

# person = "John"
# greet(person)

# greet("hello" + " world")


# def calculate_discount(user_age, is_student, total_purchase_amount):
#     discount_percentage = 0.0

#     if user_age < 18:
#         if is_student:
#             discount_percentage = 10.0  # 10% discount for students under 18
#         else:
#             discount_percentage = 5.0   # 5% discount for non-student minors
#     elif user_age >= 50:
#         discount_percentage = 15.0      # 15% discount for adults

#     discounted_amount = total_purchase_amount * (discount_percentage / 100)

#     if discount_percentage > 0:
#         return f"You are {user_age} years old {'and also a student ' if is_student else ''}and purchased {total_purchase_amount}, so you have a {discount_percentage}% discount. You save ${discounted_amount:.2f}."
#     else:
#         return "No discount applied."


# # # Test cases
# print(calculate_discount(17, True, 100.0))
# print(calculate_discount(17, False, 100.0))
# print(calculate_discount(70, False, 100.0))


# def calculate_discount(user_age, is_student, total_purchase_amount):
#     discount_percentage = 0.0

#     if user_age < 18 and is_student:
#         discount_percentage = 10.0  # 10% discount for student minors
#     elif user_age < 18:
#         discount_percentage = 5.0   # 5% discount for non-student minors
#     elif user_age >= 50:
#         discount_percentage = 15.0  # 15% discount for adults

#     discounted_amount = total_purchase_amount * (discount_percentage / 100)

#     if discount_percentage > 0:
#         return f"You are {user_age} years old {'and also a student ' if is_student else ''}and purchased {total_purchase_amount}, so you have a {discount_percentage}% discount. You save ${discounted_amount:.2f}."
#     else:
#         return "No discount applied."


# # Test cases
# print(calculate_discount(17, True, 100.0))
# print(calculate_discount(17, False, 100.0))
# print(calculate_discount(70, False, 100.0))
