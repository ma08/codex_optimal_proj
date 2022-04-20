
def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1, n):
        a = set(s[:i])
        b = set(s[i:])
        ans = max(ans, len(a & b))
    print(ans)

if __name__ == "__main__":
    main()
