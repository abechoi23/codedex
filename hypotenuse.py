""" 09. Pythagorean Theorem
# User Input
Thus far, we've only been outputting things to the user, making our programs one-sided and not that fun. Almost every popular website, mobile app, or video game today has both input and output. So how do we get input from the user?

Python uses the input() function to get user input.

username = input('Enter your name: ')

print(username)

The output will say "Enter your name: " and the user can type in something, hit enter, and whatever the user typed gets stored into the variable username.

So here, suppose the user typed in their own name and pressed enter, it will output their name.

The whole process looks like this in VS Code:

Input Example

If you're using the Code Input on Codédex on the right👉, make sure to watch this video.

By default, the user input is stored as a text string, which is working great for now.

But what about when we want to get a number from a user?

In that case, we would need to wrap an int() around the input() to convert the text string into a number:

age = int(input('What\'s your age: '))

print(age)

Now that the user types 24 and press enter, the age variable will be an integer 24, and not a text string "24".

# Instructions
If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

The equation has the form of:


a 
2
 +b 
2
 =c 
2
 

Take a closer look at this formula:

The a is the length of a short side.
The b is the length of a short side.
The c is the length of the hypotenuse.
The hypotenuse is the side that's opposite of the right angle. It's also longest side of the right triangle.

Create a hypotenuse.py program that asks the user for two numbers, a and b, and calculates the hypotenuse using the Pythagorean equation, rewritten like so:


c= 
a 
2
 +b 
2
 
​
 

Bonus: If you can solve this problem and are still looking for a challenge, try the Quadratic formula after! """

def hypotenuse(a, b):
    c = (a**2 + b**2)**0.5
    return c

a = int(input('Enter a number in digits for side a: '))
b = int(input('Enter a number in digits for side b: '))

c = hypotenuse(a, b)
print(f'The length of the hypotenuse is {c}.')
