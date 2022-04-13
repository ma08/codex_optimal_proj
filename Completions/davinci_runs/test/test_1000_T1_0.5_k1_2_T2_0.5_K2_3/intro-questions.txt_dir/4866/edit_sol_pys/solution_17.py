import sys

def is_halloween(date):
    month, day = date.split(" ")
    month = month.upper()
    day = int(day)

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
