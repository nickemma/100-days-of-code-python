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
