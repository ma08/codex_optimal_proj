

month, day = input().split()  # input month and day
if (month == "OCT" and day == "31") or (month == "DEC" and day == "25"):  # if month is october and day is 31 or month is december and day is 25
    print("yup")
else:
    print("nope")
