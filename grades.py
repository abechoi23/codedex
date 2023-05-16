""" 12. Grades
# If Statement
An if statement is used to test a condition for truth and execute the code if it is True:

if condition:
  # code inside

For example, if the grade variable is greater than 60:

if grade > 60:
  print("You passed!")

Note: The code "inside" the if statement must be indented (preferably 2 spaces).

# Else
An else clause can be optionally added to an if statement.

If the condition evaluates to True, code in the if part is executed.
If the condition evaluates to False, code in the else part is executed.
if grade > 60:
  print("You passed.")
else:
  print("You failed.")

# Instructions
Holy moly, because the whole class's average was low on the test, the teacher just added in a curve for the test grades!

Create a grades.py program that checks whether a grade is above or below 55.

Start by creating a variable called grade and give it a value that's between 0 and 100.

Write a if/else statement for the following:

If grade is greater than or equal to 55, then print "You passed."
Else, print "You failed."
After you run the code, change grade's value and run it again. Do this a few times to make sure it's working as intended. """

import random

grade = random.randint(0, 100) 

def test_grades():
    if grade >= 55:
        print(f'You passed with a grade of {grade}%.')
    else:
        print(f'You failed with a grade of {grade}%.')

test_grades()