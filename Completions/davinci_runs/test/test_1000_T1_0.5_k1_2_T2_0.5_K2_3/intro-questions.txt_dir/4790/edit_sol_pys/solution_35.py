import sys

def main():
    for s in sys.stdin:
        s = s.strip()
        if s.count('B') == s.count('W'):
            print(1)
            continue
        if s[0] == s[-1]:
            if s.count(s[0]) == len(s) - 1:
                print(1)
                continue
        print(0)

if __name__ == "__main__":
    main()
