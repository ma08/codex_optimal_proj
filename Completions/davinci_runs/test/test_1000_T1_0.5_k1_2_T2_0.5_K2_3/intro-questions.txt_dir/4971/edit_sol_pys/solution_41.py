
import random

def main():
    n = int(input())
    a = [i for i in range(1, n+1)]
    random.shuffle(a)
    a.sort()
    return a

print(main())
