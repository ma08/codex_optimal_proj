

import sys

def main():
    n, x, y = [int(i) for i in sys.stdin.readline().split()]
    num = sys.stdin.readline().strip()
    #print(n, x, y)
    #print(num)
    #print(num[y:x])
    #print(num[y:x].count('0'))
    print(num[y:x].count('0'))

main()