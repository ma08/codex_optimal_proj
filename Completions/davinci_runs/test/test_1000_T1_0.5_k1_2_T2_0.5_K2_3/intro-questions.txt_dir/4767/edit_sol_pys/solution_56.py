
import sys

def compute(r):
    # if the top register is full, we can't do any more
    if r[-1] == 18: return 0
    # otherwise, we can do as many more as we can increment the top register
    # without overflowing
    return 19 - r[0]

def main():
    r = [int(x) for x in sys.stdin.readline().split()]
    print(compute(r))

if __name__ == '__main__':
    main()
