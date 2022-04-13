
def main():
    n = int(input())
    a = list(map(int, input().split()))
    day = 1
    while day <= n:
        if day > a[day - 1]:
            break
        day += 1
    print(day - 1)

if __name__ == '__main__':
    main()
