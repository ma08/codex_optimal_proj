



def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(sorted(input()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
