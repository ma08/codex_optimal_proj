

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1, n):
        if s[i-1] != s[i]:
            ans += 1
    print(ans)

    if a == b:
        print(4 * a)
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
