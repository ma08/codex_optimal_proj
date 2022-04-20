

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * n
    for i in range(n - 1):
        s[i + 1] = s[i] + a[i]
    d = {}  # key: sum, value: index
    for i in range(n):
        if s[i] in d:  # sumが一致したら
            d[s[i]].append(i)  # indexを追加
        else:  # sumが一致しなかったら
            d[s[i]] = [i]  # indexを追加
    print(sum(len(d[i]) - 1 for i in d))

if __name__ == '__main__':
    main()
