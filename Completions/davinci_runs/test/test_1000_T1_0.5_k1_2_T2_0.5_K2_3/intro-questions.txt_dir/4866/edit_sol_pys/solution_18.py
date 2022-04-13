

if __name__ == "__main__":
    date = input().upper().strip()
    month, day = date.split(" ")
    if (month == "OCT" and day == "31") or (month == "DEC" and day == "25") or (month == "JAN" and day == "1"):
        print("yup")
    else:
        print("nope")
