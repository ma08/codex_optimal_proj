

def main():
    a, b, c = map(int, input().split())
    max_days = 0
    for i in range(1, 8):
        days = a // i + b // i + c // i
        if days > max_days:
            max_days = days
    print(max_days)

if __name__ == '__main__':
    main()