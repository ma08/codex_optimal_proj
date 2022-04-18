

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    s = [c for c in s]
    s.sort()
    s = "".join(s)
    print(s)

    curr = s[0]
    prev = s[0]
    res = 1
    i = 1
    while i < len(s):
        if s[i] != prev:
            res += 1
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1

    print(res)

main()
