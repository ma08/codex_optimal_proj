
import math

def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(b)
    else:
        print(b + c)

if __name__ == '__main__':
    main()
