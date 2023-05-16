""" 13. pH Levels
# Relational Operators
A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
# Elif
One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional condition(s) to check. Sometimes two is simply not enough.

if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')

# Instructions
In chemistry, pH is a scale used to specify the acidity or basicity of a liquid.

Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

First, create a variable called ph and ask the user for a value between 0 and 14.

Write an if, elif, else statement that:

If ph is greater than 7, output "Basic".
If ph is less than 7, output "Acidic".
Else, output "Neutral". """

import random

question = input('Ask any Yes or No question: ')

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question: ' + question) 
print('Magic 8 Ball: ' + answer)