from collections import Counter

def main():
    N = int(input())
    S = [input() for i in range(N)]
    c = Counter(S)
    ans = 0
    for i in c.values():
        if i >= 2:
            ans += (i * (i - 1)) // 2
    print(ans)

if __name__ == '__main__':
    main()
