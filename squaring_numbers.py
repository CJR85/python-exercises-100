# Write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the numbers list but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do NOT change code above

# Write code below:
squared_numbers = [num * num for num in numbers]
# Write code above

print(squared_numbers)