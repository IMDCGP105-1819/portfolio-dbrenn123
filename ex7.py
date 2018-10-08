## House deposit save time calculator
DEPOSIT_RATE = 0.2
SAVINGS_INTEREST_RATE = 0.04

# Get required data from user
total_cost = float(input("Enter house price (£#.##): £"))
salary = float(input("Enter your annual salary (£#.##): £"))
saved_portion = float(input("Enter amount to be saved: %")) / 100

# Calculate required values
savings_target = total_cost * DEPOSIT_RATE
monthly_savings = salary * saved_portion / 12
