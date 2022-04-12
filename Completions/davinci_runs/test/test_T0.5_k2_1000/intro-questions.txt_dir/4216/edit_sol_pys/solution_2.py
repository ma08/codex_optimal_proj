
import math

def main():
    N = int(input())
    r = int(math.ceil(math.sqrt(N)))
    for i in range(r, 1, -1):
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1), end='')

            break

if __name__ == '__main__':
    main()
