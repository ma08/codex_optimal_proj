
import sys

def main():
    n = int(sys.stdin.readline().strip())
    q = [int(x) for x in sys.stdin.readline().strip().split()]
    if len(q) != (n-1):
        print("-1")
        return
    if n == 2:
        print("-1")
        return
    p = []
    p.append(1)
    for i in range(n-1):
        p.append(p[i]+q[i])
    if any([(x<1) or (x>n) for x in p]):
        print("-1")
        return
    if len(set(p)) != n:
        print("-1")
        return
    for i in p:
        print(i, end=" ")

if __name__ == "__main__":
    main()