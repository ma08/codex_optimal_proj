

import sys

def is_diverse(s):
    if len(s) == 1:
        return True
    i = 0
    while i < (len(s) - 1):
        if ord(s[i+1]) - ord(s[i]) != 1:
            return False
        i += 1
    return True

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        s = sys.stdin.readline().strip()
        if is_diverse(s):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()