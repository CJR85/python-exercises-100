# Write a program that prints each number betweeen 1 to 100 in turn.
# When the number is divisible by 3, then instead of printing the number, it should print "Fizz".
# When the number is divisible by 5, the instead of printing the number, it should print "Buzz".
# When the number is divisible by both 3 and 5, the instead of printing the number, it should print "FizzBuzz".

# Write code below

for number in range(1, 101):
    # Divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
