
from collections import Counter

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    res = 0
    for i in c.keys():
        res += c[i] * (c[i] - 1)
    print(res)

if __name__ == '__main__':
    main()
