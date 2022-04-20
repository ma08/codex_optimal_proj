
import math
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()
    if n == 1:
        print(1)
        return
    i = 0
    j = n-1
    count = 0
    while i < j:
        if a[i] + a[j] == 2**int(math.log(a[i]+a[j],2)): # check if a[i] + a[j] is a power of 2
            i += 1
            j -= 1
        elif a[i] + a[j] > 2**int(math.log(a[i]+a[j],2)):
            j -= 1
            count += 1
        else:
            i += 1
            count += 1
    if i == j:
        count += 1
    print(count)

if __name__ == "__main__":
    main()
