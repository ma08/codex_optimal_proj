
import sys

def main():
    k = int(input())
    x = int(7 % k)
    i = 1
    while True:
        if x % k == 0:
            print(i)
            return
        x = int(x * 10 + 7)
        i += 1

if __name__ == '__main__':
    main()
