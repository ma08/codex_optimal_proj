
def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 1
    prev = a[0]
    for i in range(n):
        if a[i] != prev:
            cnt += 1
            prev = a[i]
    print(cnt)

if __name__ == '__main__':
    main()
