
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    n = int(readline())
    d = [int(i) for i in readline().split()]
    d.sort()
    ans = 0
    for i in range(n-1):
        ans += d[i+1] - d[i]
    print(ans)

if __name__ == "__main__":
    main()
