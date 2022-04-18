
import sys

def main():
    try:
        k = int(sys.stdin.readline().strip())
        n = 0
        while 2**n < k:
            n += 1
        print(2**n, n)
    except:
        print('error')

if __name__ == '__main__':
    main()
