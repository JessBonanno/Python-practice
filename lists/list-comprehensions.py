# list comprehension iterates into a list with less code than a for loop
nums = [1, 2, 3]
print([x * 10 for x in nums])

name = 'colt'
print([char.upper() for char in name])

# can add conditional logic
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
print(evens)
# if else statement in list comprehension
# for every num in numbers times by 2 if even divide by 2 if odd
print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])

with_vowels = 'This is so much fun!'
# removes vowels from string and creates list with rest of chars
print(' '.join([char for char in with_vowels if char not in 'aeiou']))

# ! exercises
names = ['Elie', 'Tim', 'Matt']
# create a new list containing the first letter of each name in the list
answer1 = [name[0] for name in names]
print(answer1)
numbers = [1, 2, 3, 4, 5, 6]
# create a new list of all the even values
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6]
# create a new list that is the intersection of nums1 and nums2
# output should be [3,4]
answer = [num for num in nums1 if num in nums2]
print(answer)
words = ['Elie', 'Tim', 'Matt']
# create a new list where each name in words is reversed and lowercase
answer2 = [word[::-1].lower() for word in words]
print(answer2)

# for all numbers between 1 and 100 inclusive create a variable called answer that contains a list of all the numbers that are divisible by 12
answer = [num for num in list(range(1, 101)) if num % 12 == 0]
print(answer)

# givin the string 'amazing' create a variable called answer containing all the letters from 'amazing' but not the vowels
answer = [letter for letter in 'amazing' if letter not in 'aeiou']
print(answer)

# ! end exercises

# nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])  # first list second element
print(nested_list[1][-1])  # second list last element
# print all values from nested_list with nested loop
for l in nested_list:
    for val in l:
        print(val)
# nested list comprehension
[[print(val) for val in l] for l in nested_list]

# generating a list with lists from 1-3 x 3
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)
# nested comprehension puls conditional logic
# for each list if num is odd its X else its O 
# repeats 3xs
print([["X" if num % 2 != 0 else "O" for num in range(1, 4)]
       for val in range(1, 4)])

# ! exercises

# using a nested list comprehension and range create a variable called answer containing [[0,1,2],[0,1,2],[0,1,2]]
answer = [[num for num in range(3)] for val in range(3)]
print(answer)
answer = [[num for num in range(10)] for val in range(10)]
print(answer)