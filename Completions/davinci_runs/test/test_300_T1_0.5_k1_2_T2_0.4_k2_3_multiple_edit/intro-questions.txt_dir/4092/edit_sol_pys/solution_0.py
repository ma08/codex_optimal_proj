
import sys

def main():
    n = sys.stdin.readline().rstrip()
    n = int(n.strip())
    a = sys.stdin.readline()
    a = a.split(" ")
    for i in range(n):
        a[i] = int(a[i].strip())
    print(a)

if __name__ == '__main__':
    main()
