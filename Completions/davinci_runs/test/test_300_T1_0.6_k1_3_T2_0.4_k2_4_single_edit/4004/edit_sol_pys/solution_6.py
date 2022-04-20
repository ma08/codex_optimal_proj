

def solve(n, s):
    if n == 1:
        if s[0] == "0":
            return "0"
        else:
            return "1"
    else:
        if s[-1] == "0":
            return solve(n-1, s[:-1])
        else:
            return "1" + solve(n-1, s[:-1])



def solve2(n, s):
    if n == 1:
        if s[0] == "0":
            return "0"
        else:
            return "1"
    else:
        if s[0] == "0":
            return solve2(n-1, s[1:])
        else:
            return "1" + solve2(n-1, s[1:])


n = int(input())
s = input()

print(solve(n, s))
print(solve2(n, s))
