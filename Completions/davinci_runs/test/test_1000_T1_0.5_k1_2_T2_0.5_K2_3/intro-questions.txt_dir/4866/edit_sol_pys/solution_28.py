

month, day = input().split(' ')
if month == "OCT" and day == "31" or month == "DEC" and day == "25" or month == "AUG" and day == "31" or month == "JAN" and day == "1":
    print("yup")
else:
    print("nope")
