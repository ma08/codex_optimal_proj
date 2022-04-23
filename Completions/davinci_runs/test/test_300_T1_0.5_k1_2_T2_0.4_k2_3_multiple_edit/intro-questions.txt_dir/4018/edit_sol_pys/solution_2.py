

def main():
    n, k = map(int, input().split())  # k is the number of distinct characters
    s = input()

    if k > (1 << n):
        print(-1)
        return

    s = sorted(s)
    # print(s)

    curr = s[0]
    prev = s[0]
    res = 0
    i = 1
    while i < len(s):
        if s[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    print(res, end="")

main()
