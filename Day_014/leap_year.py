# as we have already done it in Day_5 leapyear.py we will be usig new approach here  ie.  making a leap year function

# Logic/Condition = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year,"is a leap year.")
else:
   print(year,"is'nt a leap year.")
