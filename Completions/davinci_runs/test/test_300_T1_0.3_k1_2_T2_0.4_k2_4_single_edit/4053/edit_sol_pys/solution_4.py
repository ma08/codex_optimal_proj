def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            if s1[i:] == s2:
                return True
    return False



def solve(n, prefixes, suffixes):
    for i in range(2*n-2):
        if i < n-1:
            print("P", end="")
        else:
            print("S", end="")


if __name__ == "__main__":
    n = int(input())
    prefixes = []
    suffixes = []

    for i in range(2*n-2):
        s = input()
        if len(s) == 1:
            prefixes.append(s)
        else:
            suffixes.append(s)

    solve(n, prefixes, suffixes)
