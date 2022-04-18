
import sys, math

def main():
    n = int(input())
    t = list(map(int,input().split()))
    t.sort()
    if n % 2 == 0:
        for i in range(n):
            print(t[int(i/2)], end=" ")
            if i % 2 == 0:
                print(t[int(n/2) - int(i/2) - 1], end=" ")
    else:
        for i in range(n):
            print(t[int(i/2)], end=" ")
            if i % 2 == 0:
                print(t[int(n/2) - int(i/2)], end=" ")

if __name__ == "__main__":
    main()
