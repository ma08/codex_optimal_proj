

def main():
    n = int(input())
    s = input()
    t = input()
    ans = sum([1 for i in range(n) if s[i] != t[i]])
    for i in range(n):
        if s[:i] == t[:i] and s[i:] == t[i+1:]:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
