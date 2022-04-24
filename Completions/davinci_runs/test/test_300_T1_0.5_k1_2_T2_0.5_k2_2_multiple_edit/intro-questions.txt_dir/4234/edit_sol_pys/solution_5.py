import sys

def main():
    n = int(input())
    s = input()
    good = True
    i = 0
    while i < len(s)-1:
        if s[i] == s[i + 1]:
            good = False
            break
        i += 2
    if good:
        print(0)
        print(s)
    else:
        print(len(s)-i)
        print(s[:i] + s[i+1:])

if __name__ == '__main__':
    main()
