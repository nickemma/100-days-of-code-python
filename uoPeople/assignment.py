def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(3)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)


countup(-3)

# Function to perform countdown from a positive number


def countdown(num):
    print("Counting down from", num)
    for i in range(num, 0, -1):
        print(i)
    print("Blastoff!")

# Function to perform countup from a negative number


def countup(num):
    print("Counting up from", num)
    for i in range(num, 0):
        print(i)
    print("Blastoff!")


# Get a number from user input
num = float(input("Enter a number: "))

if num > 0:
    countdown(int(num))
elif num < 0:
    countup(int(num))
else:
    print("Zero entered. Choosing to call countdown from zero.")

# Explanation for calling countdown from zero:
# We chose to call the `countdown` function for input of zero because counting down from zero is a more intuitive concept than counting up from zero in most scenarios. While you could choose to call `countup` for zero, it's a less common use case and might not be as expected.

# Function to perform division with potential division by zero error


def divide_numbers():
    # Get user input for num and den
    num = int(input("Enter the num: "))
    den = int(input("Enter the den: "))

    try:
        # Attempt the division operation
        result = num / den
        print("Result:", result)
    except ZeroDivisionError as e:
        # Handle division by zero error
        print("Error: Division by zero occurred.")
    except ValueError as e:
        # Handle invalid input error (e.g., non-integer values)
        print("Error: Invalid input. Please enter valid numbers.", e)
    except Exception as e:
        # Handle unexpected errors
        print("An unexpected error occurred:", e)


# Call the function to trigger potential errors
divide_numbers()

# Explanation: Error handling in expressions or conditions is a crucial aspect of programming because it allows developers to gracefully handle unexpected situations and prevent their programs from crashing. Let's use the division by zero scenario as an example to discuss the significance of error handling, and I'll provide detailed explanations and code snippets to guide junior developers. In the code dividing a number by zero is mathematically undefined and can lead to runtime errors. Without proper error handling, attempting to divide by zero can result in program crashes, unexpected termination, and potentially data loss or corruption. Let's see the code snippet below to understand the importance of error handling.

# Code Without Error Handling:
# num = 10 and den = 0
# result = num / den  # Potential division by zero error
# In this code, we are attempting to divide num by den, where den is zero. Without error handling, Python would raise a ZeroDivisionError at the point of division, and the program would terminate abruptly.

# Code With Error Handling:
# numerator = 10
# denominator = 0

# try:
#     result = numerator / denominator
#     print("Result:", result)
# except ZeroDivisionError as e:
#     print("Error: Division by zero occurred.")
# Here, we use a try-except block to handle the division by zero scenario. If a ZeroDivisionError occurs, we catch the error, print a meaningful error message, and gracefully continue the program. This prevents the program from crashing.


# Function to perform division with explicit condition checks


def divide_numbers():
    num = input("Enter the num: ")
    den = input("Enter the den: ")

    if den == '0':
        print("Error: Division by zero is not allowed.")
    elif not num.isdigit() or not den.isdigit():
        print("Error: Please enter valid numerical values.")
    else:
        num = int(num)
        den = int(den)
        result = num / den
        print("Result:", result)


# Call the function to perform division
divide_numbers()
