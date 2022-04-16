

month, day = input().split()[:2]
if (month == "OCT" and day == "31") or (month == "DEC" and day == "25"):
    print("yup")
else:
    print("nope")
