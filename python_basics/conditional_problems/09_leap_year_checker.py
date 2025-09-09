# Problem: Determine if a year is a lead year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year_in = int(input("Enter the year:\t"))

if (year_in % 400 == 0) or ((year_in % 4 == 0) and (year_in % 100 != 0)):
    print(f"{year_in} is a Leap Year")
else: print(f"{year_in} is not a Leap Year")