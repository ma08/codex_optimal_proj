
import math

def main():
    n = int(input()) # input as a string
    count = 0
    if n <= 1:
        print(n)
        return
    while n > 0:
        if n % 6 == 0:
            n = n // 6
            count += 1
        elif n % 9 == 0:
            n = n // 9
            count += 1
        else:
            n = n - 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()
