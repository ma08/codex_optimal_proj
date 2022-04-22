import sys

def main():
    k = int(input())
    x = 7 % k
    i = 0
    while True:
        i += 1
        if x % k == 0:
            print(i)
            return
        x = (x * 10 + 7) % k

if __name__ == '__main__':
    main()
