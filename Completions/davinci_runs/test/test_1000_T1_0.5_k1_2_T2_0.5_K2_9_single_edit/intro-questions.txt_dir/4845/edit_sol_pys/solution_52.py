
def main():
    """Determine the day of the week."""
    day, month = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    total = 0
    for i in range(month - 1):
        total += days[i]
    total += day
    print(week[(total - 1) % 7])

main()
