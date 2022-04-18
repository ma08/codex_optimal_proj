
import sys

def max_allowance(a, b, c):
    return max(a+b+c, a*10+b+c, a+b*10+c, a*10+b*10+c, (a+b)*10+c, a*10+(b+c), a*100+b+c, a*10*10+b+c)

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    print(max_allowance(a, b, c))
