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

# Track savings over time
current_savings = monthly_savings
total_time = 0

# Increment time until target savings reached
while(current_savings < savings_target):
    current_savings += (current_savings * SAVINGS_INTEREST_RATE) + monthly_savings
    total_time += 1

# Display results
print(f"Deposit: £{savings_target: .2f}")
print(f"Monthly Savings: £{monthly_savings: .2f}")
print(f"Time: {total_time} months")
