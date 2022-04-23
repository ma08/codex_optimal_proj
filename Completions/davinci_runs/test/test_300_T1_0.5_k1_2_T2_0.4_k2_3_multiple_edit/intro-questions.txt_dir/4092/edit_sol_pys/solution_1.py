
import sys

def main():
    n = sys.stdin.readline().strip()
    n = int(n)
    a = sys.stdin.readline().strip()
    a = a.split()
    for i in range(n):
        a[i] = int(a[i])
    print(a)

if __name__ == '__main__':
    main()
