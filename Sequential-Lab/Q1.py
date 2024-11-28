# Write a whole positive number and calculate if it's pair or not.
number1=int(input("Type your number: "))

# Test if number is pair or not...
if number1 % 2 ==0:
    print(f"{number1} is pair.")
else:
    print(f"{number1} is odd.")