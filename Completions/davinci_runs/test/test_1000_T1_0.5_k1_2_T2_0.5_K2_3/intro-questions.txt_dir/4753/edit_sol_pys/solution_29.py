
import sys

def main():
    n = int(sys.stdin.readline())
    if n == 3:
        print(0)
    elif n == 4: 
        print(1)
    else:
        print((n-3)*(n-2)*(n-4)/2)

main()
