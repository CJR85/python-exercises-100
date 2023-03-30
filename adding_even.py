# Write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.
# Important: There should only be ONE print statement in the console output

# Write code below

# Solution 1
total = 0
for number in range(2, 101, 2):
    total += number
print(total)