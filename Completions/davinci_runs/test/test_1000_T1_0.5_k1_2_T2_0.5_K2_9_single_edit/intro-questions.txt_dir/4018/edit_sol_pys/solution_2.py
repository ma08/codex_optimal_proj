

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    t = [c for c in s]
    t.sort()
    t = "".join(t)
    print(t)

    curr = t[0]
    prev = t[0]
    res = 0
    i = 1
    while i < len(t):
        if t[i] != prev:
            res += len(curr)
            curr = ""
        prev = t[i]
        curr += t[i]
        i += 1
    res += len(curr)

    print(res)

main()
