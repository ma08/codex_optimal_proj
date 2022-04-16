

import sys

def is_halloween(date):
    month, day = date.split()  # month, day = "OCT 31".split() ==> month = "OCT", day = "31"
    month = month.upper()  # month = "OCT".upper() ==> month = "OCT"
    day = int(day)  # day = "31".int() ==> day = 31

    if month == "OCT" and day == 31:
        return "yup"
    elif month == "DEC" and day == 25:
        return "yup"
    else:
        return "nope"

def main():
    date = sys.stdin.readline().strip()
    print(is_halloween(date))

if __name__ == "__main__":
    main()
