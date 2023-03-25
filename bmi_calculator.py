# Don't change the code below
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# Don't change the code above

# Write code below

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)