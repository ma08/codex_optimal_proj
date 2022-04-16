

from datetime import timedelta, date

def get_new_date(direction, days, months, years):
    current_date = date(years, months, days)
    if direction == "F": current_date += timedelta(days=1)
    else: current_date -= timedelta(days=1)
    return current_date

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        direction, days, months, years = input().split()
        days, months, years = int(days), int(months), int(years)
        new_date = get_new_date(direction, days, months, years)
        print(new_date.day, new_date.month, new_date.year)

if __name__ == "__main__":
    main()
