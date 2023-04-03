# Instructions: You are painting a wall. The instructions on the can of paint says "ONE can of paint can cover 5 square metres of wall". Given a random height & width of wall, calculate how many cans of paint you'll need to buy.

# Write the code below
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")



# Write the code above

# 🚨 Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)