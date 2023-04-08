# Instructions: Read the code below, spot the problem and modify the code to fix the program.

year = input("Which year do you want to check? ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")