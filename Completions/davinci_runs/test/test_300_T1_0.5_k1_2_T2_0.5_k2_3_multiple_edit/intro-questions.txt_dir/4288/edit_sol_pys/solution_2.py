def main():
    N = int(input())
    S = [input() for _ in range(N)]


    for s in S:
        if s[0] == s[1] and s[1] == s[2]:
            print('No')
            return
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()
