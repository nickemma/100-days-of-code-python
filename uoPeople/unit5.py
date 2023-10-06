# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False


# print(any_lowercase1('UoPeople'))
# print(any_lowercase1('uoPeople'))


# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'


# print(any_lowercase2('UoPeople'))
# print(any_lowercase2('uoPeople'))


# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag


# print(any_lowercase3('Programming'))
# print(any_lowercase3('programminG'))

# Explanation: This function will check each letter of the string and return True if the last letter is lowercase and False if the last letter is uppercase. The output will be False and True.


# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag


# print(any_lowercase4('Python'))
# print(any_lowercase4('python'))
# print(any_lowercase4('PYTHON'))


# Explanation: This function will check each letter of the string and return True if any of the letters are lowercase and False if all of the letters are uppercase. The output will be False and True.

# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True


# print(any_lowercase5('Coding'))
# print(any_lowercase5('coding'))

# Explanation: This function will check each letter of the string and return False if any of the letters are uppercase and True if all of the letters are lowercase. The output will be False and True.

# Input your name
# name = input("Enter your name: ")

# # Display n characters from the left (Accept n as input)
# n = int(input("Enter the number of characters to display from the left: "))

# # use slicing method (name[:n]) to extract the first n characters from the name string. The result is stored in the left_characters variable and displayed to the user.
# left_characters = name[:n]
# print(f"{n} characters from the left: {left_characters}")

# # Count the number of vowels
# vowels = "AEIOUaeiou"
# vowel_count = sum(1 for char in name if char in vowels)
# print(f"Number of vowels in your name: {vowel_count}")

# # Reverse your name
# reversed_name = name[::-1]
# print(f"Reversed name: {reversed_name}")
# To reverse your name, we use slicing with a step of -1 (name[::-1]). This step retrieves all characters in reverse order and stores them in reversed_name, which is then displayed.

# Explanation: The program asks the user to enter their name and the number of characters to display from the left. The program then displays the first n characters from the left, the number of vowels in the name, and the name in reverse order (from right to left) using slicing with a step of -1.
