

def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n):
        print(-1)
        return

    s_list = [c for c in s]
    s_list.sort()
    s_list = "".join(s_list)
    print(s_list)

    curr = s_list[0]
    prev = s_list[0]
    res = 0
    i = 1
    while i < len(s_list):
        if s_list[i] != prev:
            res += len(curr)
            curr = ""
        prev = s[i]
        curr += s[i]
        i += 1
    res += len(curr)

    print(res)

main()
