# Instructions: Prime numbers are numbers that can only be cleanly divisble by itself & 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it is only divisible by 1 & 2.
# But 4 is not because you can didvide it by 1, 2 or 4.

# Write your code below
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
      if  number % i == 0:
        is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        



# Write your code above

# Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)