# # hypotenuse function step by step, including code and test cases:

# # Stage 1: Function Declaration


# def hypotenuse(length1, length2):
#     pass

# # Explanation: In the first stage, I defined the hypotenuse function that takes two arguments, length1 and length2, representing the lengths of the hypotenuse of a right triangle.

# # Stage 2: Calculate the Squares of the Lengths of the Sides of the Triangle


# def hypotenuse(length1, length2):
#     length1_squared = length1 ** 2
#     length2_squared = length2 ** 2
#     pass

# # Explanation: In the second stage, I calculated the squares of the lengths of the sides of the triangle and assigned them to the variables length1_squared and length2_squared.


# # Stage 3: Calculate the Sum of the Squares of the Lengths of the Sides of the Triangle
# def hypotenuse(length1, length2):
#     length1_squared = length1 ** 2
#     length2_squared = length2 ** 2
#     sum_of_squares = length1_squared + length2_squared
#     pass

# # Explanation: In the third stage, I calculated the sum of the squares of the lengths of the sides of the triangle and assigned it to the variable sum_of_squares.

# import math
# # Stage 4: Calculate the Hypotenuse of the Triangle
# def hypotenuse(length1, length2):
#     length1_squared = length1 ** 2
#     length2_squared = length2 ** 2
#     sum_of_squares = length1_squared + length2_squared
#     hypotenuse_length = math.sqrt(sum_of_squares)
#     return hypotenuse_length

# # Explanation: In the final stage, we import the math module to use the sqrt function and calculate the hypotenuse length using the Pythagorean theorem. Then, we return the hypotenuse length.


# # Test Cases:
# print(hypotenuse(3, 4))
# print(hypotenuse(5, 12))
# print(hypotenuse(8, 15))

# # Explanation: In the test cases, we call the hypotenuse function with different arguments and print the results.

# part 2
# Stage 1: Function Declaration

def calculate_discount(price, discount_percentage):
    pass

# Explanation: In the first stage, I defined the calculate_discount function that takes two arguments, price and discount_percentage, representing the price of an item and the discount percentage.

# Stage 2: Calculate the Discount Amount


def calculate_discount(price, discount_percentage):
    discount_amount = (price * discount_percentage) / 100
    pass

# Explanation: In the second stage, I calculated the discount amount and assigned it to the variable discount_amount.

# Stage 3: Calculate the Discounted and Final Price


def calculate_discount(price, discount_percentage):
    discount_amount = (price * discount_percentage) / 100
    final_price = price - discount_amount
    pass

# Explanation: In the third stage, I calculated the discounted price and assigned it to the variable final_price.


# Stage 4: Return the Result
def calculate_discount(price, discount_percentage):
    discount_amount = (price * discount_percentage) / 100
    final_price = price - discount_amount
    return final_price

# Explanation: In the final stage, we return the final price.


# Test Cases:
print(calculate_discount(100, 10))
print(calculate_discount(200, 15))
print(calculate_discount(300, 20))
