

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    ss = [c for c in s]
    ss.sort()
    ss = "".join(ss)
    print(ss)

    curr = ss[0]
    prev = ss[0]
    res = 0
    i = 1
    while i < len(ss):
        if ss[i] != prev:
            res += len(curr)
            curr = ""
        prev = ss[i]
        curr += ss[i]
        i += 1
    res += len(curr)

    print(res)

main()
