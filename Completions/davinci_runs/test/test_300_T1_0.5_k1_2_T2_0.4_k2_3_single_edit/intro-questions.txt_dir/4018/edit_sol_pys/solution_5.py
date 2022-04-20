

def main():
    n, k = map(int, input().split())
    S = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    S = [c for c in S]
    S.sort()
    S = "".join(S)
    print(S)

    curr = S[0]
    prev = S[0]
    res = 0
    i = 1
    while i < len(S):
        if S[i] != prev:
            res += len(curr)
            curr = ""
        prev = S[i]
        curr += S[i]
        i += 1
    res += len(curr)

    print(res)

main()
