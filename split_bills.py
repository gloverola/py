# Replace ___ with your code

# get input value for total number of friends
total_friends = int(input("Total number of friends: "))

# get input value for bill
bill = int(input("What is your total bill: "))

# calculate the tax amount
tax_amount = (bill * 0.2)
total_amount = bill + tax_amount

# divide the total bill among friends
split_amount = total_amount / total_friends

# print the split amount
print(f"Each friend should pay: {split_amount:.2f}")