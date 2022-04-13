

def main():
    """Determine the day of the week.
    Args:
        x (int): day
        y (int): month
    Returns:
        day of the week
    x = int(input())
    y = int(input())
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # number of days in each month
    week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]  # days of the week
    total = 0  # total number of days passed
    for i in range(y - 1):
        total += days[i]  # add the number of days passed in each month
    total += x  # add the number of days passed in this month
    print(week[(total - 1) % 7])  # print the day of the week

main()
