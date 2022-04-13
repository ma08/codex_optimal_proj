

# My code here!
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    S_sort = set()
    for s in S:
        S_sort.add(''.join(sorted(s)))
    ans = 0
    for s in S_sort:
        c = 0
        for s_ in S:
            if ''.join(sorted(s_)) == s:
                c += 1
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()
