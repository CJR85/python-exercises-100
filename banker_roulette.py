# Write a program which will select a random name from a list of names. The person picked will have to pay for everybody's food bill.
import random
# Split string method
names_string = input("Give me every name, separated by a comma.")
names = names_string.split(",")
# Don't change the code above

# Write code below
# Get the total number of items in the list
# num_items = len(names)
# # Generate random numbers between 0 and the last index
# random_choice = random.randint(0, num_items - 1)
# bill_payer = names[random_choice]

bill_payer = random.choice(names) # Choice function
print(bill_payer + " is going to pay for the entire meal today.")
