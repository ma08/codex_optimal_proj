import math

def main():
    n = int(input())
    r = math.ceil(math.sqrt(n))
    for i in range(r, 0, -1): # rから1までの逆順
        if n % i == 0:
            print(n // i // 10 ** (len(str(i)) - 1))
            break

if __name__ == '__main__':
    main()
