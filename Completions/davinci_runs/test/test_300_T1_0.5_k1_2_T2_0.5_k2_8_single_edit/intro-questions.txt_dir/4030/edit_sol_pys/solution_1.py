

def solve(n, s):
    if (n == 1):
        return 1
    if (n == 2):
        if (s[0] < s[1]):
            return 1
        else:
            return 2
    if (n == 3):
        if (s[0] < s[1] and s[1] < s[2]):
            return 1
        elif (s[0] < s[1] and s[1] > s[2]):
            return 2
        elif (s[0] > s[1] and s[1] < s[2]):
            return 2
        else:
            return 3
    if (s[0] == s[1]):
        return 1
    if (s[0] < s[1]):
        return 1
    if (s[1] < s[2]):
        return 1
    if (s[2] < s[3]):
        return 1
    if (s[3] < s[4]):
        return 1
    if (s[4] < s[5]):
        return 1
    if (s[5] < s[6]):
        return 1
    if (s[6] < s[7]):
        return 1
    if (s[7] < s[8]):
        return 1
    return 2

def main():
    n = int(input())
    s = input()
    ans = solve(n, s)
    print(ans)
    if (ans == 1):
        print(1, 1, 1, 1, 1, 1, 1, 1, 1)
    else:
        print(1, 2, 1, 2, 1, 2, 1, 2, 1)

if __name__ == "__main__":
    main()
