# use randint(a, b) to generate a random number between a and b
from random import randint
res = input('how hows it going? ')
while res != 'stop copying me':
    res = input(f'{res} \n')
print('you win!')

i = 1
while i < 5:
    i + i


number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint(1, 10)
    i += 1
