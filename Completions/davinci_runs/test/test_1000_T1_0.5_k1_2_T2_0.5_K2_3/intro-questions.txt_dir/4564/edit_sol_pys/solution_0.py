import sys

def is_unique(s):
    if len(s) > 26:
        return False
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

def main():
    s = sys.stdin.readline().rstrip()
    if is_unique(s):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
