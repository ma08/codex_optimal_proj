
import sys
from collections import defaultdict
 
def main():    
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    d = defaultdict(int)
    for i in range(n):
        d[a[i] + b[i]] += 1
    print("%d %d" % (n - max(d.values()), n // 2 - d["RS"] - d["SR"]))
 
if __name__ == '__main__':
    main()
