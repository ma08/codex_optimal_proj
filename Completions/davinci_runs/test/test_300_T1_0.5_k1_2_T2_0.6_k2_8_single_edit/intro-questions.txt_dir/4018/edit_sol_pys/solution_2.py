

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return
    curr_len = 1

    s = [c for c in s]
    s.sort()
    s = "".join(s)
    print(s)

    curr = s[0]
    prev = s[0]
    res = curr_len
    i = 1
    while i < len(s):
        if s[i] != prev:
            res += curr_len
            curr = s[i]
            curr_len = 1
        else:
            curr += s[i]
            curr_len += 1
        prev = s[i]
        i += 1

    print(res)

main()
