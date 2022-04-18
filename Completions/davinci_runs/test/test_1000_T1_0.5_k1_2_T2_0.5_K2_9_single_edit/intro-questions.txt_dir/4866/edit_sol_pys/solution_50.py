

import sys

month_dict = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

def is_halloween(date):
    month, day = date.split()
    day = int(day)
    month = month_dict[month]

    if (day == 31 and month == 10) or (day == 25 and month == 12):
        print("yup")
    else:
        print("nope")

def main():
    date = sys.stdin.readline().strip()
    is_halloween(date)

if __name__ == "__main__":
    main()
