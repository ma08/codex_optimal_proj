

#The answer is:
"""
import sys

def hailstone(n):
    if n == 1: return 1
    elif n % 2 == 0: return n + hailstone(n//2)
    else:
        return n + hailstone(3*n+1)

def main():
    for line in sys.stdin:
        n = int(line)
        print(hailstone(n))

if __name__ == '__main__':
    main()
"""
