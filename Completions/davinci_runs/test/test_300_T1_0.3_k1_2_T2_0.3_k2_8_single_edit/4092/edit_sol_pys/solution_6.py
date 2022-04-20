

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * n
    for i in range(n):
        s[i] = s[i - 1] + a[i]
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = i
        else:
            print(i - d[s[i]])
            return
    print(0)

if __name__ == '__main__':
    main()
