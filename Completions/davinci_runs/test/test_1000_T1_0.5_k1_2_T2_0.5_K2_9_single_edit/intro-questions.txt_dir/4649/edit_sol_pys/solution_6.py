

def rgb_substring(s, k):
    s_len = len(s)
    if k > s_len:
        return -1
    if k == s_len:
        return 0
    if k == 1:
        return 1
    if k == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if k == 3:
        if s[0] == s[1] or s[1] == s[2]:
            return 1
        else:
            return 0
    if k == 4:
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
            return 1
        elif s[0] == s[1] and s[1] == s[2] and s[2] != s[3]:
            return 1
        elif s[0] == s[1] and s[1] != s[2] and s[2] == s[3]:
            return 1
        elif s[0] != s[1] and s[1] == s[2] and s[2] == s[3]:
            return 1
        elif s[0] == s[1] and s[1] != s[2] and s[2] != s[3]:
            return 2
        elif s[0] != s[1] and s[1] == s[2] and s[2] != s[3]:
            return 2
        elif s[0] != s[1] and s[1] != s[2] and s[2] == s[3]:
            return 2
        else:
            return 0
    if k == 5:
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[3] and s[3] == s[4]:
            return 1
        elif s[0] == s[1] and s[1] == s[2] and s[2] == s[3] and s[3] != s[4]:
            return 1
        elif s[0] == s[1] and s[1] == s[2] and s[2] != s[3] and s[3] == s[4]:
            return 1
        elif s[0] == s[1] and s[1] != s[2] and s[2] == s[3] and s[3] == s[4]:
            return 1
        elif s[0] != s[1] and s[1] == s[2] and s[2] == s[3] and s[3] == s[4]:
            return 1
        elif s[0] == s[1] and s[1] == s[2] and s[2] != s[3] and s[3] != s[4]:
            return 2
        elif s[0] == s[1] and s[1] != s[2] and s[2] == s[3] and s[3] != s[4]:
            return 2
        elif s[0] == s[1] and s[1] != s[2] and s[2] != s[3] and s[3] == s[4]:
            return 2
        elif s[0] != s[1] and s[1] == s[2] and s[2] == s[3] and s[3] != s[4]:
            return 2
        elif s[0] != s[1] and s[1] == s[2] and s[2] != s[3] and s[3] == s[4]:
            return 2
        elif s[0] != s[1] and s[1] != s[2] and s[2] == s[3] and s[3] == s[4]:
            return 2
        elif s[0] == s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
            return 3
        elif s[0] != s[1] and s[1] == s[2] and s[2] != s[3] and s[3] != s[4]:
            return 3
        elif s[0] != s[1] and s[1] != s[2] and s[2] == s[3] and s[3] != s[4]:
            return 3
        elif s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] == s[4]:
            return 3
        else:
            return 0
    return 0


def main():
    q = int(input())
    for _ in range(q):
        n, k = [int(x) for x in input().split()]
        s = input()
        print(rgb_substring(s, k))


if __name__ == "__main__":
    main()
