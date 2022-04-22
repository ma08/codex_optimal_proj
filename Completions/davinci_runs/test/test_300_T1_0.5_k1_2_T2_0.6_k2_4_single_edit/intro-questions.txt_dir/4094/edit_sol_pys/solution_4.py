import sys

def main():
    k = int(input())
    num = 7
    count = 1
    while True:
        if num % k == 0:
            print(count)
            return
        num = num * 10 + 7
        count += 1

if __name__ == '__main__':
    main()
