""" 17. Enter PIN
# Loop
In programming, a loop is used to repeat a block of code until a specified condition is satisfied. It's another tool that's used a ton!

People will often use the generic term “iterate” when referring to loops; iterate simply means “to repeat”.

The first kind of loop that we are going to learn is the while loop. You can think of the while loop like a traffic circle.

Each lap is one iteration! The car will iterate over and over again until it can't do so anymore.

roundabout example
# Instructions
Before we dive deep into the while loop, let's see a demo using a bank's ATM. 🏦

Create an enter_pin.py program and type in the following:

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

Try the following in the code input window to the right 👉:

Type 1111 and then the enter key.
Type 2023 and then the enter key.
Type 1991 and then the enter key.
Type 1234 and then the enter key. """

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')
