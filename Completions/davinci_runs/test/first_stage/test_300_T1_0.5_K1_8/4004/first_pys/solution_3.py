
import sys
def main():
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    print(minD(a))

def minD(a):
    if (len(a) == 1):
        return 0
    a.sort()
    m = a[0]
    for i in range(1,len(a)):
        m = gcd(m,a[i])
    if m == 1:
        return -1
    return m

def gcd(a,b):
    while (b != 0):
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()