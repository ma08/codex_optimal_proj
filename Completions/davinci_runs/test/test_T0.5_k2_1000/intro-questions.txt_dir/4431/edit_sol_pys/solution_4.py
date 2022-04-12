

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    c = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if set(s[i:j]) <= set(k):
                c += 1
    print(c)

if __name__ == "__main__":
    main()
