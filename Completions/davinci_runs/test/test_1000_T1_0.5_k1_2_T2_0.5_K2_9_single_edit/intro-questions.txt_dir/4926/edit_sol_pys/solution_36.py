
import sys

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def euler(x):
    euler = 0
    for i in range(0, x+1):
        euler += 1 / factorial(i)
    return euler

def main():
    x = int(sys.stdin.readline().strip())
    print(euler(x))

if __name__ == '__main__':
    main()
