# Learned about CONTROL FLOWS

countries = ['united states', 'canada', 'france',
             'italy', 'china', 'japan', 'brazil', 'nigeria']
print(len(countries))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
['a', 'b', 'c']
print(x[0][2])

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# birth_year = input('what is your birth year? ')

# age = 2023 - int(birth_year)

# print(f'My age is {age}')
