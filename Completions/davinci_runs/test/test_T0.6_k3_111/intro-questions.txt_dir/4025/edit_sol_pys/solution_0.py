

def main():
    a, b, c = map(int, input().split())  # a, b, c are the number of days that a, b, c can work per week
    max_days = 0
    for i in range(1, 8):  # i is the number of days that the work can be done per week
        days = a // i + b // i + c // i  # the number of days that the work can be done per week
        if days > max_days:
            max_days = days
    print(max_days)

if __name__ == '__main__':
    main()
