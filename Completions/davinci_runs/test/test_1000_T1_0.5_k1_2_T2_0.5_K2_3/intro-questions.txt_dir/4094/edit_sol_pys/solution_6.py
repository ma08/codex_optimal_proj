
import sys

def main():
    k = int(input())
    x = 7 % k
    n = 1
    while True:
        if x == 0:
            print(n)
            return
        x = (x * 10 + 7) % k
        n += 1

if __name__ == '__main__':
    main()
