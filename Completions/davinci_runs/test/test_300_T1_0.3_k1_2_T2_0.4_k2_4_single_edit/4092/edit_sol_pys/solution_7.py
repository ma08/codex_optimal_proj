

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}
    for j in range(n + 1):
        if s[j] not in d:
            d[s[j]] = j
        else:
            print(j - d[s[j]])
            return
    print(0)

if __name__ == '__main__':
    main()
