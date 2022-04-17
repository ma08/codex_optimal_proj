

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    s_ = [c for c in s]
    s_.sort()
    s_ = "".join(s_)
    print(s_)

    curr = s_[0]
    prev = s_[0]
    res = 0
    i = 1
    while i < len(s_):
        if s_[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    print(res)

main()
