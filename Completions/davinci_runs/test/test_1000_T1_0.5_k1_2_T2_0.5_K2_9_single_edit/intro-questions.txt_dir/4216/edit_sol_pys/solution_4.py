
import math

def main():
    N = int(input())
    for i in range(math.ceil(math.sqrt(N)), 0, -1):
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1))
            break

if __name__ == '__main__':
    main()
