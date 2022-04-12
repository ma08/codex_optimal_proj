def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == "R":
            if i+1 < n and s[i+1] == "R":
                ans += 1
        elif s[i] == "G":
            if i+1 < n and s[i+1] == "G":
                ans += 1
            if i+2 < n and s[i+2] == "G":
                ans += 1
        elif s[i] == "B":
            if i+1 < n and s[i+1] == "B":
                ans += 1
            if i+2 < n and s[i+2] == "B":
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
