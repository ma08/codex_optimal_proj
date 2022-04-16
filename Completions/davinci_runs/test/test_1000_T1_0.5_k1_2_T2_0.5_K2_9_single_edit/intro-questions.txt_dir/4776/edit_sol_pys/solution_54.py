
import sys

def main():
    n = int(sys.stdin.readline().strip())
    days = []
    for i in range(n):
        s, t = map(int, sys.stdin.readline().strip().split())
        for j in range(s, t+1):
            if j not in days:
                days.append(j)
    print(len(days), days)

if __name__ == '__main__':
    main()
