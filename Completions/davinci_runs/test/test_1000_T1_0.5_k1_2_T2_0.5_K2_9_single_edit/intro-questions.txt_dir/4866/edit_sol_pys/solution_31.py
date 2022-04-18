

def main():
    import sys
    month_dict = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}

    def is_halloween(date):
        month, day = date.split()
        day = int(day)
        month = month_dict[month]

        if (day == 31 and month == "10") or (day == 25 and month == "12"):
            print("yup")
        else:
            print("nope")

    date = sys.stdin.readline().strip()
    is_halloween(date)

main()
