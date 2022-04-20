
def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)  # s[i] = a[0] + a[1] + ... + a[i - 1]
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}  # d[s[i]] = i
    for i in range(n + 1):
        if s[i] not in d:
            d[s[i]] = i
        else:
            print(i - d[s[i]])
            return
    print(0)

if __name__ == '__main__':
    main()
