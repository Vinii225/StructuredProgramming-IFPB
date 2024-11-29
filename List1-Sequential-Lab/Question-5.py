# Question-5
# One enterprise defined different cashbacks based on purchase price, show cashback in the final.

#                       Purchase Value - Cashback
#                            Until 100.00 -> 4%
#               Between 100.01 and 200.00 -> 6%
#               Between 200.01 and 400.00 -> 8%
#                            Above 400.00 -> 10%

# Get purchase value.
purchase_value=float(input("Type your purchase value: "))

# Verify cashback.
if purchase_value<=100:
    cashback_value = purchase_value * 0.04
elif purchase_value<=200:
    cashback_value = purchase_value * 0.06
elif purchase_value<=400:
    cashback_value = purchase_value * 0.08
elif purchase_value>400:
    cashback_value = purchase_value * 0.10

# Show cashback.
print(f"The cashback is: {cashback_value:.2f}")

