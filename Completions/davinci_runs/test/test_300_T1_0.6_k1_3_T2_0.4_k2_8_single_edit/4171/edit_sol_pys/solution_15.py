
import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()
    i = 0 #number of elements that are less than the last element
    while a[i] < a[n-1]:
        a[i] = a[i]//2
        i += 1 #increment i
    print(i) #print i


if __name__ == '__main__':
    main()
