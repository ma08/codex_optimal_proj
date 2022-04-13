
import sys

def is_harshad(n):
    return n % sum([int(i) for i in str(n)]) == 0

def next_harshad(n):
    n += 1
    while not is_harshad(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline())
    print(next_harshad(n))

if __name__ == "__main__":
    main()
