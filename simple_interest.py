# Simple Interest Calculator

# take float input for principal, rate, and time
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))

# calculate the simple interest
simple_interest = principal * rate * time * .01

# calculate the final amount
final_amount = principal + simple_interest

# print interest and total_sum in separate lines
print(simple_interest)
print(final_amount)