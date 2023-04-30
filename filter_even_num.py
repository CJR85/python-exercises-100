# TODO: Write a List Comprehension to create a new list called result. This new list should contain the even numbers from the list.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do NOT change code above

# Write code below
result = [num for num in numbers if num % 2 == 0]
# Write code above

print(result)