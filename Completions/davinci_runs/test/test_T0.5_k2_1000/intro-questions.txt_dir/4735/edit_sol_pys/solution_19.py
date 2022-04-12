def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    # else:
    #     leap = False

    return leap


year = int(input("Enter a year: "))  # 1900
print(is_leap(year))
