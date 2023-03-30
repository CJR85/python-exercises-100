# Write a program that calculates the average student height from a list of heights.
# The average height can be calculated by adding all the heights together & dividing by the total number of heights.

# 🚨Don't change code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨Don't change code above

# Total number of heights
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# Total number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# Average height of students
average_height = round(total_height / number_of_students)
print(average_height)
# Write code solution below