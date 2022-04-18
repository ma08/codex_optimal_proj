

def main():
    n, k = map(int, input().split())
    s = input()

    s = [c for c in s]
    s.sort()
    s = "".join(s)
    print(s[0] + "".join(sorted(s[1:])))

main()
