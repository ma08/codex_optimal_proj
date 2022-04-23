


def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(str(input()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
