
import sys

def main():
    k = int(input())
    n = 0
    while 2**n < k: 
        n += 1
    print(2**n)
    print(n)

if __name__ == '__main__':
    main()
