import sys

def main():
    s, v1, v2 = map(float, sys.stdin.readline().split())
    if s % (v1 + v2) == 0:
        print(s // (v1 + v2), 0)
    elif s % v2 == s % (v1 + v2):
        print(s // (v1 + v2), (s % (v1 + v2)) // v2)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()
