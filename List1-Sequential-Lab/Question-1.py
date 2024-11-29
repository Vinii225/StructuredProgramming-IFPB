# Question-1
# Read a whole positive number and calculate if it's pair or not.

# Get number
number1=int(input("Type your number: "))

# Test if number is pair or not and show it.
if number1 % 2 ==0:
    print(f"{number1} is pair.")
else:
    print(f"{number1} is odd.")