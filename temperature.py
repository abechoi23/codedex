""" 06. Data Types
# Variables
In programming, variables are used for storing data values. Each variable has a name and they hold a value.

The variable name can consist of letters, numbers, and the _ underscore character.

These are all valid variable names and values:

name = 'Sonny Li'
user_id = 16180339887
progress = 0.75
exp = 60
verified = True

The = equal sign means assignment:

We are assigning the string value 'Sonny Li' to the variable name.
We are assigning the number value 16180339887 to the variable user_id.
We are assigning the number value 0.75 to the variable progress.
We are assigning the number value 60 to the variable exp.
We are assigning the truth value True to the variable verified.
We can also change the value of a variable, or print it out:

xp = 70

xp = 80

print(xp)    # Output: 80

Here, we are assigning the number value 70 to the variable xp. Then, we are reassigning the integer value 80 to the same variable. And printing it out.

# Data Types
## Int
An integer, or int, is a whole number. It has no decimal point and contains the number 0, positive and negative counting numbers. If we were counting the number of people on the bus or the number of jellybeans in a jar, we would use an integer.

year = 2023
age = 32

## Float
A floating-point number, or a float, is a decimal number. It can be used to represent fractions or precise measurements. If you were measuring the length and width of the window, calculating the average test score, or storing a baseball player’s batting average, we would use a float instead of an int.

pi = 3.14159
meal_cost = 12.99

## String
A string, or str, is used for storing text. Strings are wrapped in double quotes " " or single quotes ' '.

message = "good nite"
user = '@sonnynomnom'

## Boolean
A Boolean data type, or bool, stores a value that can only be either true or false. In Python, it's capitalized True or False. It's named after the British mathematician George Boole (1815-1864).

late_to_class = False
cranky = True

07. Temperature
# Operators
Computers are incredible at doing math calculations. Now that we have learned about variables, let's use them with arithmetic operators to calculate things!

Python has the following arithmetic operators:

+ Addition
- Subtraction
* Multiplication
/ Division
% Modulo (returns the remainder)
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1

And take a look at this code that calculates a 20% tip by calculating the total and then multiplying by a float (decimal number):

pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print(tip) # Output: 0.796

Another way to write this is using parentheses to calculate the total and the tip in one line of code:

tip = (pizza + coke) * 0.2

In Python, parentheses have the highest order of operations.

Now that we've learned about the basics of variables and operators, let's put them to use!

# Instructions
Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in Python:


Celsius= 
1.8
(Fahrenheit−32)
​
 
Print out the converted temperature. """


def temperature(F):
    celsius = (F - 32) / 1.8
    return celsius

F = 57

celsius = temperature(F)

print(f'{F}°F is equal to {round(celsius)}°C.')