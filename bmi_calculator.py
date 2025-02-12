# BMI Claculator
# take float input for weight
weight = float(input("What is your weight: "))

# take float input for height
height = float(input("What is your height: "))

# calculate BMI
bmi = weight / (height ** 2)

# print the calculated BMI
print(bmi)