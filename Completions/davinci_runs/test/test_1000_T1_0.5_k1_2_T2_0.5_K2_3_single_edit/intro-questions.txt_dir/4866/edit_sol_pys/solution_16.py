

month, day = input().split() # split input into month and day
if month in ["OCT", "DEC"] and day == "25": # if the month is october or december and the day is 25
    print("yup")
else:
    print("nope")
