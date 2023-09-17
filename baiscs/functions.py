# Functions

# def my_func(name):
#     print(f'hello {name}')
#     print(f"It's good to have you around mr {name}")


# my_func('techieEmma')

print('Welcome to auth with python')

username = input('What is your username? ')
password = input('What is your password? ')

print('Account created successfully...')
print('login with your credentials')

username2 = input('Login with your username?\n')
password2 = input('Login with your password?\n')

if username == username2 and password == password2:
    print('User logged in successfully')
else:
    print('Invalid credentials Email or Password')


# def formated_string(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid input?"

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"


# print(formated_string(input("What is your first Name? "),
#       input("what is your last Name? ")))
