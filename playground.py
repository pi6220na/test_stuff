import pprint
from birdseye import eye

pp = pprint.PrettyPrinter(indent=4)

# Formatting strings in Python

characterInfo = { 'Cloud' : 7, 'Squall' : 8 }

#Below the 2 For Loops result in the same output
#The first example uses addition signs to form a string
for char in characterInfo:
    print('Name: ' + char + ' is level ' + str(characterInfo[char]))

print()

# Curly brackets take the place of variables and addition signs
# You only need one set of quotations followed by .format(var1, var2)
# It automatically formats the characterInfo[char] to a string as well
# Great way to display menus, try adding :10 in the first set of brackets to see what happens
for char in characterInfo:
    print('Name: {:10} is level {}'.format(char, characterInfo[char]))






@eye
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

my_func(name='tim', sport='football', roll=19)

g = globals()
l = locals()
pp.pprint(g)
pp.pprint(l)

