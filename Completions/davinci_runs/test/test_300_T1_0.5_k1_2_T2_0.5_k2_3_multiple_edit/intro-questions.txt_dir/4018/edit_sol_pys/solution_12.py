

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n):
        print(-1)
        return

    s = sorted(s)

    curr = s[0][0]
    prev = s[0][0]
    res = 0
    for i in s:
        for j in i:
            if j != prev:
                res += len(curr)
                curr = ""
            prev = j
            curr += j
    res += len(curr)

    print(res)

main()
