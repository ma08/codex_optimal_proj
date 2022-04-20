

def main():
    n = int(input())
    s = input()
    stack = 0
    ans = 0
    for i in range(n):
        if s[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack == -1:
            ans += 1
        if stack < 0:
            stack = 0
    print(ans)

if __name__ == "__main__":
    main()