import random
print('Welcome to the number guessing game!')
print('I am thinking of a number between 1 and 100.')
# Import the random module

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# set difficulty
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print('Invalid input. Try again.')
    exit()

# set attempts
print(f'You have {attempts} attempts remaining to guess the number.')

# set guess
guess = int(input('Make a guess: '))
while attempts > 0:
    if guess == secret_number:
        print(f'You got it! The answer was {secret_number}.')
        exit()
    elif guess > secret_number:
        print('Too high.')
        attempts -= 1
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
    elif guess < secret_number:
        print('Too low.')
        attempts -= 1
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))

print(f'You ran out of guesses. The answer was {secret_number}.')
