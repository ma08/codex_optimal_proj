
import sys

month_dict = {"JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12"}

def is_halloween(date):
    month, day = date.split() # split the date string into a month and a day
    day = int(day) # convert the day to an integer
    month = month_dict[month] # convert the month from a string to a number

    if (day == 31 and month == "10") or (day == 25 and month == "12"): # check if the date is either 10/31 or 12/25
        print("yup") # if it is, print "yup"
    else:
        print("nope") # if it isn't, print "nope"

def main():
    date = sys.stdin.readline().strip() # read in the date from the user as a string
    is_halloween(date) # call is_halloween and give it the date string

if __name__ == "__main__":
    main()
