def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i + 1 == a[i]:
            continue
        if i + 2 == a[i]:
            a[i], a[i+1] = a[i+1], a[i]
        else:
            print(-1)
            exit()
    print(sum(a[i] != i+1 for i in range(n)))

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    day = 1
    while day <= n:
        if day > a[day-1]:
            break
        day += 1
    print(day-1)

if __name__ == '__main__':
    main()
