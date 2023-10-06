def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


print(any_lowercase1('UoPeople'))
print(any_lowercase1('uoPeople'))


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


print(any_lowercase2('UoPeople'))
print(any_lowercase2('uoPeople'))


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


print(any_lowercase3('Programming'))
print(any_lowercase3('programminG'))


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print(any_lowercase4('Python'))
print(any_lowercase4('python'))
print(any_lowercase4('PYTHON'))


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


print(any_lowercase5('Coding'))
print(any_lowercase5('coding'))


# Input your name
name = input("Enter your name: ")

# Display n characters from the left (Accept n as input)
n = int(input("Enter the number of characters to display from the left: "))

# use slicing method (name[:n]) to extract the first n characters from the name string. The result is stored in the left_characters variable and displayed to the user.
left_characters = name[:n]
print(f"{n} characters from the left: {left_characters}")

# Count the number of vowels
vowels = "AEIOUaeiou"
vowel_count = sum(1 for char in name if char in vowels)
print(f"Number of vowels in your name: {vowel_count}")

# Reverse your name
reversed_name = name[::-1]
print(f"Reversed name: {reversed_name}")
