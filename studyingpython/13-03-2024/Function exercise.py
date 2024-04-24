#"write a program to find the given year is a leap year or not"

#year = int(input("enter a year: "))

#if  (year % 4 == 0 year % 100 != 0) or (year % 400 == 0):
    #print(year, "It is a gap year")

#else:
    #print(year, "It is not a gap year")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

year = int(input("Enter a year: "))
is_leap_year(year)
