# Instructions: Convert the function is_leap_year() so that instead of printing "Leap year" or "Not leap year", it should return TRUE if it IS a leap year & return FALSE otherwise.
# Then create a function called days_in_month() which will take the year & month as inputs.


# Write code below

def is_leap_year(year):
  if year % 4 == 0:
      # Is year divisble by 100?
      if year % 100 == 0:
          # Is year divisble by 400?
          if year % 400 == 0:
              return True
          else:
              return False
      else:
        return True
  else:
    return False

def days_in_month(year, month):
  #  if month > 12 or month < 1:
  #     return "Invalid month"
   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
   if is_leap_year(year) and month == 2:
      return 29
   return month_days[month - 1]
      

# DO NOT change the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

