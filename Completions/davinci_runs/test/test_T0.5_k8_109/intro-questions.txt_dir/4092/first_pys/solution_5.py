

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    s = 0
    used = set()
    for i in range(n):
        s += a[i]
        if s == 0 or s in used:
            ans += 1
            s = 0
            used = set()
        used.add(s)
    print(ans)

if __name__ == "__main__":
    main()