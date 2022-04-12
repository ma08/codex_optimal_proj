

def rgb_substrings(s, k):
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
    return -1


def main():
    q = int(input())
    for _ in range(q):
        n, k = [int(x) for x in input().split()]
        s = input()
        print(rgb_substrings(s, k))


if __name__ == "__main__":
    main()
