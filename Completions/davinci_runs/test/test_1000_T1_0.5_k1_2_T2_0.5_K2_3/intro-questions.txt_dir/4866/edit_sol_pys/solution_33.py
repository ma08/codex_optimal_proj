def special_day(month, day):
    if (month == "OCT" and day == "31") or (month == "DEC" and day == "25") or (month == "JAN" and day == "1"):
        return "yup"
    else:
        return "nope"

if __name__ == "__main__":
    date = input().upper()
    month, day = date.split(" ")
    print(special_day(month, day))
