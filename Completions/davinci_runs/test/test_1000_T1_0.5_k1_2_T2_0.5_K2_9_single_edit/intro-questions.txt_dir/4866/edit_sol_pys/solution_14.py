def check_date(month, day):
    if (month == "OCT" and day == "31") or (month == "DEC" and day == "25"):
        print("yup")
    else:
        print("nope")


if __name__ == "__main__":
    date = input()
    month, day = date.split()
    check_date(month, day)
