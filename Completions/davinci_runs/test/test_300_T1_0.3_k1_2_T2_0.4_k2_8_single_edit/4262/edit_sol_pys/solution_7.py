
import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))  # p[i] = i+1
    q = list(map(int, input().split()))  # q[i] = i+1
    print(abs(p.index(1) - q.index(1)))  # abs(p.index(1) - q.index(1))

if __name__ == '__main__':
    main()
