
# * similar to js objects but keys should be in quotes unless a number
from random import choice  # DON'T CHANGE!
user_info = {
    'name': 'jess',
    'age': 38,
    'is awesome': True
}

artist = {
    "first": "Neil",
    "last": "Young",
}

# ! exercise
# declare a variable called full_name that is equal to artist's first and last names with a space between by referencing the values associated with those in artist dictionary
full_name = artist['first'] + ' ' + artist['last']
# if doing fstring don't forget inner quotes cant match outter quotes
full_name = f"{artist['first']} {artist['last']}"
print(full_name)
# ! end exercise

# * iterating dictionaries
# access all values
for v in user_info.values():
    print(v)
# access all keys
for v in user_info.keys():
    print(v)
# access all items (key value pairs)
# no order guaranteed
for k, v in user_info.items():
    print(f'key is {k}, value is {v}')

# ! exercise
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for v in donations.values():
    total_donations += v
print(total_donations)
# ! end exercise

# * check dictionary to see if it contains a specific key
# returns true or false
print('name' in user_info)
# same thing for keys
print('jess' in user_info.values())

# * dictionary methods

# * clear
# empties dict
print(user_info.clear())
print(user_info)

user_info = {
    'name': 'jess',
    'age': 38,
    'is awesome': True
}

# * copy makes a copy
clone = user_info.copy()
print(clone)

# * fromkeys creates key-value pairs from comma separated values
print({}.fromkeys(['email'], 'unknown'))
print({}.fromkeys('a', [1, 2, 3, 4, 5, ]))
new_user = {}.fromkeys(['name', 'score', 'email'], 'unknown')
print(new_user)
# if the first item isn't a list but a string it will iterate over the string creating values for each letter
no_list_fromkeys = {}.fromkeys('iterate', 'values')
print(no_list_fromkeys)

# * get retrieves a keys value in an object and return None instead of KeyError if it doesn't exist
print(user_info.get('email'))
print(user_info.get('name'))

# ! exercises
# This code picks a random food item:
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# print out a string depending on if food is a value in bakery_stock
# if food is contained in bakery_stock print out a string that states how many items are left.
# if food is not contained in bakery_stock print out "We don't make that"
# YOUR CODE GOES BELOW:
if bakery_stock.get(food) == None:
    print("We don't make that")
else:
    print(f'{bakery_stock.get(food)} left')

    # DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

# ! end exercises
