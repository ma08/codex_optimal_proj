import sys



def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def euler(x):
    e = 0
    for i in range(0, x+1):
        e += 1 / factorial(i)
    return e

def main():
    x = int(sys.stdin.readline().strip())
    print(euler(x))

if __name__ == '__main__':
    main()
