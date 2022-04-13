import math

def main():
    N = int(input())
    r = int(math.ceil(math.sqrt(N)))
    for i in range(r, 0, -1):
        if N % i == 0:
            print(int(N // i // 10 ** (len(str(i)) - 1)))
            break

if __name__ == '__main__':
    main()
