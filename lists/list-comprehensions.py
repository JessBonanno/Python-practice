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

names = ['Elie', 'Tim', 'Matt']
# create a new list containing the first letter of each name in the list
answer1 = [name[0] for name in names ]
print(answer1)
numbers = [1,2,3,4,5,6]
# create a new list of all the even values
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

nums1 = [1,2,3.4]
nums2 = [3,4,5,6]
answer = []
print(answer)
