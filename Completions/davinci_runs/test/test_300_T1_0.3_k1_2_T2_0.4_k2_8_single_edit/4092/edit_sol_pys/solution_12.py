

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)  # 前缀和
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}  # 前缀和 -> 位置
    for i in range(n + 1):
        if s[i] not in d:
            d[s[i]] = i
        else:
            print(i - d[s[i]])
            return
    print(0)

if __name__ == '__main__':
    main()
