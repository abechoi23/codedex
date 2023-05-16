""" 21. Fizz Buzz
# Congrats!
You've made it to the end of this chapter! Here's a refresher on what we went over.

The while loop iterates over and over again until the condition is no longer true:

while coffee < 1:
  print('tired')

The for loop and the range() function:

for i in range(10):
  print(i)

Logical operators, and, or, not, combine and evaluate two conditions.

Now let's take your learnings to the test!

# Instructions
Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies.

Though this challenge may appear simple to experienced coders, it is designed to weed out 90% of job candidates who cannot apply their coding knowledge to a new problem creatively.

Want to give it a try?

Create a fizz_buzz.py program that outputs numbers from 1 to 100. Here's the catch:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz". """

for i in range(1, 101):
    if i % 3 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)