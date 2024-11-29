# Read a name and age of 2 persons and show who the name of who is older.

# Name and age of person 1.
name1=str(input("Type your name: "))
age1=int(input("Type your age: "))

# Name and age of person 2.
name2=str(input("\nType your name: "))
age2=int(input("Type your age: "))

# Verify who is older and show it.
if age1>age2:
    print(f"{name1} is older than {name2}.")
elif age2>age1:
    print(f"{name2} is older than {name1}.")
