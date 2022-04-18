

month, date = input().upper().split()
if month in ["OCT", "DEC"] and date == "31":
    print("yup")
else:
    print("nope")
