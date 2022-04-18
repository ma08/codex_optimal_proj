

def get_res(s, k):
    if k > (1 << len(s)):
        return -1

    ss = [c for c in s]
    ss.sort()
    ss = "".join(ss)

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

    return res

def main():
    n, k = map(int, input().split())
    s = input()

    print(get_res(s, k))

main()
