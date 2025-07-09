import random


def guessing_game():

    answer = random.randint(0, 100)
    remaining_guesses = 2

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

    else:
        print('Your three chances are up!')

guessing_game()