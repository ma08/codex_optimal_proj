

def main():
    n, k = map(int, input().split())  # n is number of input, k is the number of distinct characters
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    sorted_s = [c for c in s]
    sorted_s.sort()  # sort the character in order
    sorted_s = "".join(sorted_s)
    print(sorted_s)

    curr = sorted_s[0]
    prev = sorted_s[0]
    res = 0
    i = 1
    while i < len(sorted_s):
        if sorted_s[i] != prev:
            res += len(curr)
            curr = ""
        prev = sorted_s[i]
        curr += sorted_s[i]
        i += 1
    res += len(curr)

    print(res)

main()
