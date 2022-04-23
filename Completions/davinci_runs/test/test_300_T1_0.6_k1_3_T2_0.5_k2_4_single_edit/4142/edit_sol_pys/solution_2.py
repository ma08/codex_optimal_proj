

from collections import deque

def main():
    s = input()
    even = deque(s[::2])
    odd = deque(s[1::2])
    print("Yes" if all(list(map(lambda x: x in "RUD", odd))) and all(list(map(lambda x: x in "LUD", even))) else "No") else "No")

if __name__ == '__main__':
    main()
