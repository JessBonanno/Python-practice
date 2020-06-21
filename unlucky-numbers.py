numbers = range(20)
for num in numbers:
    if (num % 2 == 0) and (num != 4):
        print('even')
    elif (num % 2 != 0) and (num != 13): 
        print('odd')
    else:
        print('unlucky')