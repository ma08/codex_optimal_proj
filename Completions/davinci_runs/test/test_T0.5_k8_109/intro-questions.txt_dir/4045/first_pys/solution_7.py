


def solve(n, s, t):
    if n == 1:
        return "YES\nabc"
    if n == 2:
        if s == "ab" and t == "bc":
            return "YES\nacbbac"
        if s == "ab" and t == "ca":
            return "YES\ncbabca"
        if s == "ca" and t == "ab":
            return "YES\nbcabca"
        if s == "ca" and t == "bc":
            return "YES\ncbcabca"
        if s == "bc" and t == "ab":
            return "YES\nacbcabca"
        if s == "bc" and t == "ca":
            return "YES\ncacbacbab"
        return "YES\nacabacabac"
    if n == 3:
        if s == "ab" and t == "bc":
            return "YES\nacbbacacbbac"
        if s == "ab" and t == "ca":
            return "YES\ncbabcacbabca"
        if s == "ca" and t == "ab":
            return "YES\nbcabcbabca"
        if s == "ca" and t == "bc":
            return "YES\ncbcabcbcabca"
        if s == "bc" and t == "ab":
            return "YES\nacbcabacbcabca"
        if s == "bc" and t == "ca":
            return "YES\ncacbacbcacbacbab"
        return "NO"
    if n >= 4:
        return "YES\nac" + "bc" * (n - 1) + "ac" + "bc" * (n - 1) + "ac" + "bc" * (n - 1) + "ac" + "bc" * (n - 1) + "ac"
    return "NO"


def main():
    n = int(input())
    s = input()
    t = input()
    print(solve(n, s, t))


if __name__ == "__main__":
    main()