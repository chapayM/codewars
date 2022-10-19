# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Note: For 4 or more names, the number in "and 2 others" simply increases.

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif 1 < len(names) <= 3:
        names_str = ''
        for i in range(len(names)-1):
            if len(names) == 2:
                names_str += names[i]
            elif i == 0:
                names_str += names[i] + ', '
            else:
                names_str += names[i]
        names_str += ' and ' + names[i+1]
        return f'{names_str} like this'
    else:
        names_str = names[0] + ', ' + names[1]
        num = len(names) - 2
        return f'{names_str} and {num} others like this'


print(likes([]))
print(likes(['Peter']))
print(likes(['Alex', 'Jacob']))
print(likes(['Alex', 'Jacob', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


