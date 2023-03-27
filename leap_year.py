# Write a program that works out whether if a given year is a leap year. Normal year = 365, Leap year = 366

# Don't change the code below
year = int(input("Which year do you want to check?"))
# Don't change the code above

# Write code below

# Is year divisble by 4?
if year % 4 == 0:
    # Is year divisble by 100?
    if year % 100 == 0:
        # Is year divisble by 400?
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
      print("Leap year.")
else:
  print("Not leap year.")

