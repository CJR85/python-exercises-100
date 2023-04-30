# TODO: Inside file1.txt & file2.txt are a bunch of numbers that are on single lines.
# Create a list called result which will contain the common numbers in both files.


# Write code below
with open('file1.txt') as file1:
    file_1_data = file1.readlines()

with open('file2.txt') as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
# Write code above

print(result)