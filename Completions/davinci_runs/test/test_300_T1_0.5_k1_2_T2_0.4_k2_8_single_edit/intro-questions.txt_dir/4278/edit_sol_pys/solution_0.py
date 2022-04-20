
# My code here
def main():
    N = int(input())
    S_sort = [''.join(sorted(input())) for _ in range(N)]
    from collections import Counter
    C = Counter(S_sort)
    ans = 0
    for c in C.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
