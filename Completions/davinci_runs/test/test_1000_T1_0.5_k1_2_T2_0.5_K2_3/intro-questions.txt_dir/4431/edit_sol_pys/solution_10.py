

def main():
    n, k = map(int,input().split())
    s = input()
    k = input().split()
    k = set(k)
    c = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if set(s[i:j]) <= k:
                c += 1
    print(c)

if __name__ == "__main__":
    main()
