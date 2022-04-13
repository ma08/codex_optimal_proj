

# Read input from user
y = int(input("Enter an year: "))

# Determine if the year is a leap year
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, "is a leap year.")
        else:
            print(y, "is not a leap year.")
    else:
        print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")
