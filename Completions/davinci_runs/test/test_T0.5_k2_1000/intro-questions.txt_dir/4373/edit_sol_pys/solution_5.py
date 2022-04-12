
def main():
    n = int(input())
    a = list(map(int, input().split()))
    day = 1
    while day < n and day <= a[day-1]:
        day = a[day-1] + 1
    print(day)

if __name__ == '__main__':
    main()
