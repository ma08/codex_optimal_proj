

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n):
        print(-1)
        return

    ss = [c for c in s]
    ss.sort()
    ss = "".join(ss)
    print(ss)

    curr = ""
    prev = ""
    res = 0
    i = 1
    while i < len(ss):
        if ss[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    print(res)

main()
