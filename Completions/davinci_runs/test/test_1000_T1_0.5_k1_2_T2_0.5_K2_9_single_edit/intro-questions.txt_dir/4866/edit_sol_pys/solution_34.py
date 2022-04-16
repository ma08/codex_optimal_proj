

month, day = input().split(' ')
if month == "OCT" and day == "31" or month == "DEC" and day == "25":  # check if the given date is Halloween or Christmas
    print("yup")
else:
    print("nope")
