# Functions

def my_func(name):
    print(f'hello {name}')
    print(f"It's good to have you around mr {name}")


my_func('techieEmma')

print('Welcome to auth with python')

username = input('What is your username? ')
password = input('What is your password? ')

print('Account created successfully...')
print('Now login with your credentials')

username2 = input('Login with your username?\n')
password2 = input('Login with your password?\n')

if username == username2 and password == password2:
    print('User logged in successfully')
else:
    print('Invalid credentials')
