

def solve(n, s, t):
    if s[0] == s[1] and t[0] == t[1]:
        return "NO"
    if s[0] == s[1]:
        if t[0] == t[1]:
            return "NO"
        else:
            return "".join(["a"*n, "b"*n, "c"*n])
    if t[0] == t[1]:
        return "".join(["a"*n, "b"*n, "c"*n])
    return "".join(["a"*n, "b"*n, "c"*n])

def main():
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))

if __name__ == "__main__":
    main()