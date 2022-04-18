

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    day = 1
    while day < n:
        if day < a[day-1]:
            break
        day += 1 
    print(day)

if __name__ == '__main__':
    main()
