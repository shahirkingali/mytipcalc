# This is my calucaltor project based on calculating the tip for a meal.
# The sales tax in CA is 7.25
print('Hello')
print('I will help you caluclate the tip for that delicious meal you just devoured :)')

meal = float(input("Enter your meal amount: "))
tip = int(input("Enter your tip %: "))
tax = 0.7

# Calculations
tip_amt = meal * tip/100
tax_amt = meal * tax
total = meal + tip_amt + tax_amt

print(f"Your meal was ${meal:.2f} and your tip was ${tip_amt:.2f}.")
print(f"Your total with tax was ${total:.2f}.")