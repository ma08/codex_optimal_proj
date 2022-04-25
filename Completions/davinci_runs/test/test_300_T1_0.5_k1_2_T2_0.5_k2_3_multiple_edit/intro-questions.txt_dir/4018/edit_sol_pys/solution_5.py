

def main():
    n, k = map(int, input().split())
    s = input().strip()

    if k > (1 << n) - 1:  # if k > 2^n - 1
        print(-1)
        return

    s = [c for c in s]  # string to array
    s.sort()  # sort array in place
    s = "".join(s)  # array to string

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

    print(res)

main()
