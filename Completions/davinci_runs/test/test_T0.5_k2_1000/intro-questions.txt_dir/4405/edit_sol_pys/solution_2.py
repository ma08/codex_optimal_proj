

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    s.append(-1)
    cnt = 0
    ans = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    print(ans)


if __name__ == '__main__':
    main()
