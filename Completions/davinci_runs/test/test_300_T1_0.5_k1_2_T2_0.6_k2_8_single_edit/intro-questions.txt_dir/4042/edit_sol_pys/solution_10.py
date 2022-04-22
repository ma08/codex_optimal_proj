import math

def main():
    x = float(input())

    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            print(i, int(x / i))

if __name__ == '__main__':
    main()
