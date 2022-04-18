

def main():
    """Determine the day of the week."""
    day, month = map(int, input().split())  # day and month
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]  # week days
    total = 0
    for i in range(month - 1):
        total += days[i]
    total += day
    print(week[(total - 1) % 7])

main()
