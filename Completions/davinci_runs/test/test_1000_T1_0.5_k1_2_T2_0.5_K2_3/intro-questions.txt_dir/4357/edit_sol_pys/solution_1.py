
import sys

def max_allowance(a, b, c, d):
    return max(a+b+c+d, a*10+b+c+d, a+b*10+c+d, a+b+c*10+d, a+b+c+d*10, (a+b)*10+c+d, a*10+(b+c)*10+d, a*10+b+c*10+d, a*10+b+c+d*10, a*10+(b+c+d), (a+b+c)*10+d, a*10+b*10+c+d, a*10+b+c*10+d, a*10+b+c+d*10, a*10+(b+c)*10+d, a*10+(b+c+d)*10, a*100+b+c+d, a+b*100+c+d, a+b+c*100+d, a+b+c+d*100, (a+b)*100+c+d, a*100+(b+c)*10+d, a*100+b+c*10+d, a*100+b+c+d*10, a*100+(b+c+d)*10, a*100+(b+c)*100+d, a*100+b*10+c+d, a*100+b+c*10+d, a*100+b+c+d*10, a*100+(b+c)*10+d, a*100+(b+c+d)*10, a*1000+b+c+d)

if __name__ == "__main__":
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(max_allowance(a, b, c, d))
