
import math
import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    count = 0
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    for k, v in d.items():
        count += math.factorial(v)
    print (count) % 1000000007

if __name__ == '__main__':
    main()
