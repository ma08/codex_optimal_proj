

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    n1 = a.count(a[0]) # n1 is the number of times a[0] occurs
    n2 = a.count(a[n-1]) # n2 is the number of times a[n-1] occurs
    if n1*2 == n: # if n1 is half of n
        print(n//2-1) # print n//2-1
    elif n2*2 == n: # if n2 is half of n
        print(n//2-1) # print n//2-1
    else:
        print(n-n1-n2) # print n-n1-n2

if __name__ == '__main__':
    main()
