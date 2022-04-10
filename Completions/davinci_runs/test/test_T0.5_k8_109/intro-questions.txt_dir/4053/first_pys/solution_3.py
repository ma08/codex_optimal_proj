

def main():
    n = int(input())
    prefixes = []
    suffixes = []
    for i in range(2*n-2):
        if i < n-1:
            prefixes.append(input())
        else:
            suffixes.append(input())
    print(prefixes, suffixes)
    ans = []
    for p in prefixes:
        for s in suffixes:
            if p[-1] == s[0]:
                ans.append(p+s[1:])
    print(ans)
    for a in ans:
        if len(a) == n:
            print(a)
    # print(ans)
    # for i in range(2*n-2):
    #     if i < n-1:
    #         print("P", end="")
    #     else:
    #         print("S", end="")

main()