

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1 or k == 0:
        print(-1)
        return

    string = [c for c in s]
    string.sort()
    string = "".join(string)

    curr = string[0]
    prev = string[0]
    res = 0
    i = 1
    while i < len(string):
        if string[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    print(res)

main()
