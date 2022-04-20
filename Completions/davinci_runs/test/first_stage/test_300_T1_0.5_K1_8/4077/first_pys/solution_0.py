

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    count = 0
    for i in range(n):
        if a[i] > m:
            break
        elif a[i] == m:
            count += 1

    for i in range(n):
        if a[i] > m:
            break
        elif a[i] == m:
            count += 1
        else:
            for j in range(i+1, n):
                if a[j] > m:
                    break
                elif a[j] == m:
                    count += 1
    print(count)


if __name__ == '__main__':
    main()