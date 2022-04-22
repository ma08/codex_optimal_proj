import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    a, b, c, d = map(int, readline().split())
    print(max(a * c, a * d, b * c, b * d))

if __name__ == '__main__':
    main()
