import random

random_number = random.randint(1, 10)
# handle user guesses
# if they guess correct tell them they won
# otherwise tell them if they are too high or too low
# let them play again if they want

play_again = 'yes'

while play_again == 'yes':
    random_number = random.randint(1, 10)
    guess = int(input('Guess a number between 1-10 '))
    while  guess != random_number:
        if guess > random_number:
            guess = int(input('too high, guess again! '))
        elif guess < random_number: 
            guess = int(input('too low, guess again! '))
    play_again = input('You win!  play again? ')
print('thanks for playing! ')
    
    

