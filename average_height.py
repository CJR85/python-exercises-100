# Write a program that calculates the average student height from a list of heights.
# The average height can be calculated by adding all the heights together & dividing by the total number of heights.

# 🚨Don't change code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨Don't change code above

# Write code solution below