

import sys

def main():
    n = int(sys.stdin.readline().strip())
    print(n,":",end="")
    for i in range(2,n//2+1):
        if n%i == 0 and n//i-i>=0:
            print(i,n//i,end="")
    for i in range(2,n//2+1):
        if n%i == 1 and n//i-i>=0:
            print(i,n//i,end="")

if __name__ == '__main__':
    main()
