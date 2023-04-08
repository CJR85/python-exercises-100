# Instructions: Read the code below, spot the problem and modify the code to fix the program.

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0: #Changed 'or' to 'and'
        print("FizzBuzz")
    elif number % 3 == 0: #Changed if to elif 
        print("Fizz")
    elif number % 5 == 0: #Changed if to elif
        print("Buzz")
    else:
        print(number) #Removed square brackets