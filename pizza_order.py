# Based on the user's order, work out the final bill.
# Small pizza: $15, Medium pizza: $20 & Large pizza: $25
# Pepperoni for small pizza: +$2, Pepperoni for medium & large pizza: +$3
# Extra cheese for any size pizza: + $1

# Don't change code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M or L")
add_pepperoni = input("Would you like pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
# Don't change code above

# Write code below
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")