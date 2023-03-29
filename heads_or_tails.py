# Write a virtual coin toss program.
# It will randomly tell the user "Heads" or "Tails". First letter should be capitalized

# Write code below
import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
# Hint: Remember to import the random module first