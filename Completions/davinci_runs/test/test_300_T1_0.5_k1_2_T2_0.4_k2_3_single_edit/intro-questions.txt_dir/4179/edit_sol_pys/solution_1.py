
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n-1):
        if a[i-1] < a[i] < a[i+1]:
            print("Yes")
        elif a[i-1] > a[i] > a[i+1]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
