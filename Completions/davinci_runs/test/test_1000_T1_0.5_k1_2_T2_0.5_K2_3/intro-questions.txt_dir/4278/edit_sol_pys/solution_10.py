
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    from collections import Counter
    C = Counter([''.join(sorted(s)) for s in S]) # sort all characters in s
    ans = 0
    for c in C.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
