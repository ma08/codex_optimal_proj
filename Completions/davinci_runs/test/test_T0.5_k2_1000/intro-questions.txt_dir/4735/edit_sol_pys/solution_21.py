
#The solution is to check if the year is even and if the year is divisible by 4.
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print("yes")
elif year % 400 == 0:
    print("yes")
else:
    print("no")
