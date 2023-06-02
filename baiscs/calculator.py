# CALCULATOR PROJECT DAY 10

# ADDITION
def add(n1, n2):
    return n1 + n2

# SUBTRACTION


def sub(n1, n2):
    return n1 - n2

# MULTIPLICATION


def mut(n1, n2):
    return n1 * n2

# DIVISION


def div(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": sub,
    "*": mut,
    "/": div
}

num1 = int(input("What is the first Number? "))

for symbol in operators:
    print(symbol)

operators_symbol = input("Pick any of the operators above? ")
num2 = int(input("What is the second Number? "))
calculate_function = operators[operators_symbol]
answer = calculate_function(num1, num2)


print(f"{num1} {operators_symbol} {num2} = {answer}")
