""" 10. Currency
# Congrats!
Here's a recap of everything we learned in this chapter:

Data types: int, float, str, bool.
Arithmetic operators: +, -, *, /.
The % modulo finds the remainder.
The ** exponentiation finds the exponent.
The input() function is used to get user input.
The int() function converts a value into an integer number.
# Instructions
Here's the final project of the chapter!

We just got back from a trip to Asia, specifically China, Japan, and South Korea. When we got back we have some leftover cash:

🇨🇳 Chinese yuan
🇯🇵 Japanese yen
🇰🇷 South Korean won
Create a currency.py program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.

Make sure to Google the current exchange rates!

The output of the program should look like this:

What do you have left in yuan? 560
What do you have left in yen? 2455
What do you have left in won? 3280

105.5275

The sequence should be:

Currency code example

Bonus: If you can complete this problem and you are a tryhard like me, go back to your code and try to change it into something else (crypto exchange, measurement conversion, different countries, etc.) """

def exchange_rate(yuan, yen, won):
    usd_yuan = yuan * 0.14
    usd_yen = yen * 0.0074
    usd_won = won * 0.00076
    return usd_yuan + usd_yen + usd_won

yuan = int(input('What do you have left in yuan? '))

yen = int(input('What do you have left in yen? '))

won = int(input('What do you have left in won? '))

total = exchange_rate(yuan, yen, won)

print(f'You have a total of ${total} usd.')