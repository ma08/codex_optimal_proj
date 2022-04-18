import re

def is_valid(s):
    return re.match(r"^[789]\d{9}$", s)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print("YES" if is_valid(s) else "NO")
