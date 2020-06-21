# access by index

nums = [1, 2, 3, 4]
# print by index
print(nums[0])
# access values from the end of list
print(nums[-1])  # prints last value
print(nums[-2])  # prints second to last value
# check if value is in a list
print(1 in nums)  # prints true if its in the list false if not

# print values with for loop
nums = list(range(100))
for num in nums:
    print(num)

# print values with while loop
colors = ['purple', 'teal', 'magenta', 'crimson', 'emerald']
index = 0
while index < len(colors):
    print(f'{colors[index]} at index {index}')
    index += 1

# write code that loops over the list and adds all the strings together to form one large combined string
# the combined string should be in all upppercase as well
# save result in a variable called result
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ''
for sound in sounds:
    result += sound.upper()
    print(result)

# append adds a single item to end of list
sounds.append('sound')
print(sounds)

# extend adds multiple new items to end of list
# must be inside brackets
sounds.extend(['another sound', 'and another'])
print(sounds)

# insert takes and index and item and will insert data at that index
sounds.insert(1, 'inserted')
print(sounds)

# clear removes all items from list at once
# sounds.clear()
# print(list)

# pop removes item at a specific index or last item by default if no specified index
sounds.pop(1)
print(sounds)
sounds.pop()
print(sounds)

# remove removes the first item in a list with the value of x
sounds.remove('another sound')
print(sounds)

# index will find the index of a specified item on list
print(sounds.index('sound'))
# index can also take a start point to find the index of x after a certain index (inclusive)
print(sounds.index('sound', 3))
# index can also find the index of x between a range (start and end indexes)
print(sounds.index('sound', 1, 8))

# count takes a single input and outputs the number of times it occurs in the list
print(sounds.count('sound'))

# reverse updates list with all values in reverse order
sounds.reverse()
print(sounds)

# sort will sort the list in ascending order
# same words that start with a capital will come before words starting with lowercase
sounds.sort()
print(sounds)

# join is a string method but will convert a list to a string joining them by whatever is before the .join call (the base string)
print('/'.join(sounds))


# Create a list called instructors
# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors = ['Colt', 'Blue', 'Lisa']
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
# Run the tests to make sure you've done this correctly!

# slices allow us to get a COPY of a list from start index to end index (exclusive) and can take a step interval
# WILL NOT MUTATE THE LIST
# does not use the .slice syntax, it just takes the conditions array with colons seperating params
print(sounds[2:8:2])
# must still use a colon if only looking for the start index 
# can also take a negative index to get the element from the end of list
print(sounds[-2:]) # this will return the last 2 items 
# just looking for a negative 1 step will return the list reversed
# stepping every 1 number backwards because of the negative
print(sounds[::-1])

# you can swap values by indexes (shuffling or sorting)
# Mutating the list
print(sounds)
sounds[0], sounds[1] = sounds[1], sounds[0]
print(sounds)

