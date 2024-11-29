# Read a number that is equal to a month of the year (2024 is leap year)
#  and show the quantity of days in it.

# Get month.
month=int(input("Type number of the month: "))

# Verify "month" to show the days it has.
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(f"Your month has 31 days.")
elif month==2:
    print(f"Your month has 29 days.")
elif month==4 or month==6 or month==9 or month==11:
    print(f"Your month has 30 days.")
