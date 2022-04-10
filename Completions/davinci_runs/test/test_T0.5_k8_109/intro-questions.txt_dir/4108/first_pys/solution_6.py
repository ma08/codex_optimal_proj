

import sys

def main():
    s = input()
    t = input()

    if s == t:
        print("Yes")
        sys.exit()

    for i in range(len(s)):
        if s[i] != t[i]:
            if s.count(s[i]) == t.count(t[i]) and s.count(t[i]) == t.count(s[i]):
                print("Yes")
                sys.exit()

    print("No")

if __name__ == '__main__':
    main()