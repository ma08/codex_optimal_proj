import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print("YES" if re.match(r"^[789]\d{9}$", s) else "NO") 
