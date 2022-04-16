


import sys

def main():
    s, v1, v2 = map(int, sys.stdin.readline().split())
    if s % v1 == 0:
        print(s // v1, 0)
    elif s % v2 == 0:
        print(0, s // v2)
    elif s % v2 == v1 % v2:
        print(s // v1, (s % v1) // v2)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()
