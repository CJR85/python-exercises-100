# Write a program that calculates the highest score for each student in the class.
# Important: Do not use the max or min functions.
# Output must match the example: 
# "The highest score in the class is: X"

# 🚨 Don't change the code below
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above

# Write code solution below
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")