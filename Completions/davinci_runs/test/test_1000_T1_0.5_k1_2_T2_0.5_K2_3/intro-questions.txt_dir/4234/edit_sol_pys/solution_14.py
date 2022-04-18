import sys

def main():
    n = int(input())
    s = input()
    bad = False
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            bad = True
            break
        i += 2
    if not bad:
        print(0)
        print(s)
    else:
        print(n-i)
        print(s[:i] + s[i+1:])

if __name__ == '__main__':
    main()
