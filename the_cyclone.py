""" 15. The Cyclone
# Logical Operators
One more thing that we should learn is logical operators.

Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not.

The and operator returns True if both of the conditions are True, and returns False otherwise.
The or operator returns True if at least one of the conditions is True, and returns False otherwise.
The not operator returns True if the condition is False, and reverse.
Here are some examples:

if hunger > 4 and anger > 1:
  print('Hangry')

If the hunger variable is greater than 4 and the anger variable is greater than 1, then the program prints "Hangry".

if coffee > 0 or bubble_tea > 0:
  print('☺️')

If the coffee variable is greater than 0 or the bubble_tea variable is greater than 0, then the program prints a smiley face.

if not tired:
  print('Let\'s code!')

If the tired variable is not True, then the program prints "Let's code!"

So you might be wondering: and and or are awfully similar, how do I remember the differences between the two? Let's break this down in a table form:

A	B	A and B	A or B
False	False	False	False
False	True	False	True
True	False	False	True
True	True	True	True
# Instructions
Since 1927, a rollercoaster known as "The Cyclone" has delighted riders visiting Coney Island in Brooklyn, NY. 🎢

The operator of the ride is installing a new entry system for the Cyclone (the height requirement is 137 cm and the cost to ride is 10 credits), and needs your help with writing the program for it.

Create a new file called the_cyclone.py.

Next ask the user what their height is and how many credits they have using the int() and input() functions. Make sure to store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to determine the following about a given rider:

If their height is greater than or equal to 137 and their credits is greater than or equal to 10, print "Enjoy the ride!"
Else if their height is less than 137, print "You are not tall enough to ride."
Else if their credits is less than 10, print "You don't have enough credits to ride."
Else, print "Invalid data."
Bonus: Try and create a new Boolean variable called with_taller_person and add the following control flow (which includes nested if statements):

If their height is less than 137, check the following:
If their height is less than 100 or they are not with_taller_person, print "You're not tall enough for this ride yet."
Else, if their height is greater than or equal to 100 and they are with_taller_person, print "Enjoy the ride!" """

height = int(input('Please enter in your height: '))

credits = int(input('Please enter in the remaining credits you have left: '))

with_taller_person = False 

def cyclone_entry():
    if height >= 137 and credits >= 10:
        print('Enjoy the ride!')
    elif height < 137:
        if height < 100 or not with_taller_person:
            print('You are not tall enough to ride')
        elif height >= 100 and with_taller_person:
            print('Enjoy the ride!')
    elif credits < 10:
        print('You don\'t have enough credits to ride.')
    else:
        print('Invalid Data')

cyclone_entry()