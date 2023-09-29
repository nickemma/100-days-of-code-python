# precondition: value must be greater than 0
def divide(numerator, denominator):
    if denominator == 0:
        print("Precondition violated: Division by zero is not allowed.")
        return None
    return numerator / denominator


result = divide(5, 0)
print(result)

# Postcondition violation; expected addition, not subtraction


def add(num1, num2):
    return num1 - num2


result = add(5, 3)
print(result)


def multiply(num, den):
    return num * den


result = multiply(5, 3)
# Incorrect usage; trying to concatenate a string with an integer
print(result + " uoPeople")

# Describe each possibility in your own words:
# 1. There is something wrong with the arguments the function is getting; a precondition is violated: This means that the function is receiving incorrect or unexpected input values. A precondition is a condition that must be met for a function to execute correctly. When a precondition is violated, it means the function is not getting the input it expects. This can lead to errors or unexpected behavior.

# 2. There is something wrong with the function; a postcondition is violated: This refers to a situation where the function itself is not working correctly. A postcondition is a condition that should be true after the function has been executed. When a postcondition is violated, the function is not producing the expected results or behaving as intended.

# 3. There is something wrong with the return value or the way it is being used: Even if a function works correctly, the way its return value is used in the rest of the code might be incorrect. This can lead to errors in subsequent code. It's essential to ensure that the return value of a function is used correctly and as expected.

# Define "precondition" and "postcondition" as part of your description:

# Precondition: A precondition is a condition or set of conditions that must be true before a function is executed. It specifies what the function expects in terms of input values, states, or any other relevant factors. Preconditions ensure that a function operates correctly when provided with valid input.

# Postcondition: A postcondition is a condition or set of conditions that should be true after a function has been executed successfully. It defines the expected outcomes, results, or states that the function should achieve. Postconditions help verify that a function has performed its task correctly.
