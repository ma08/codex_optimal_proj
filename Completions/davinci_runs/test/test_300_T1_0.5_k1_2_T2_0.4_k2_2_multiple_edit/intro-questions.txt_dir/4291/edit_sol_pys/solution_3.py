import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    c = list(map(int, readline().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i > 0 and a[i] == a[i-1] + 1:
            ans += c[a[i-1]-1]
    print(ans)

if __name__ == '__main__':
    main()
