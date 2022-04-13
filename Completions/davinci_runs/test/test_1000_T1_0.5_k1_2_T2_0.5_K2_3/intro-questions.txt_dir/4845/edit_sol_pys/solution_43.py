from sys import stdin

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # days in month
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # day of week

def get_day_of_week(day, month): # function to get the day of the week
    day_of_year = sum(days_in_month[:month-1]) + day # calculates the day of the year
    return day_of_week[(day_of_year + 3) % 7] # returns the day of the week

def main(): # main function
    day, month = [int(x) for x in stdin.readline().strip().split()] # gets the day and month
    print(get_day_of_week(day, month)) # prints the day of the week

if __name__ == '__main__': # if the script is run directly
    main() # run the main function
