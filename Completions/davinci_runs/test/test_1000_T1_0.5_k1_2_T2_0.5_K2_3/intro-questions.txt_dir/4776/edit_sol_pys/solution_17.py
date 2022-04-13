import sys

def main():
    n = int(sys.stdin.readline())
    days = []
    for i in range(n):
        s, t = map(int, sys.stdin.readline().split())
        for j in range(s, t + 1):
            days.append(j)
    days = set(days)
    print(len(days))

if __name__ == '__main__':
    main()
