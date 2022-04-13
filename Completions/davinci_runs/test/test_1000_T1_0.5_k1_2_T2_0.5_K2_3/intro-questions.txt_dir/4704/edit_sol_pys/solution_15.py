
import sys
readline = sys.stdin.buffer.readline

def main():
    n = int(readline())
    a = sorted(list(map(int, readline().split())))
    if a[-1] == 0:
        print(0)
    else:
        print(a[-1] - a[-2])

if __name__ == '__main__':
    main()
