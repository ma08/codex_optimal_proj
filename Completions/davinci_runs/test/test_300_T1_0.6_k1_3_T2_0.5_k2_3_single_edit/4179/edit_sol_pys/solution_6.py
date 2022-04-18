
import sys

def main(n):
    if n % 2 == 0:
        return n
    return n * 2

if __name__ == '__main__':
    n = int(input())
    print(main(n))
