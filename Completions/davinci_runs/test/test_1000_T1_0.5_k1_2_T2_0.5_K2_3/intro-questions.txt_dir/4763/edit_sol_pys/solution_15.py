
import sys

def main():
    n = int(input())
    if n == 60:
        print('single 20')
        print('triple 20')
        return
    elif n == 90:
        print('triple 20')
        print('single 20')
        return
    elif n == 180:
        print('triple 20')
        print('triple 20')
        print('triple 20')
        return
    elif n % 3 == 0:
        print('triple ' + str(n // 3))
        return
    elif n % 2 == 0:
        print('double ' + str(n // 2))
        return
    print('single ' + str(n))

if __name__ == "__main__":
    main()
