

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    n1 = a.count(a[0])
    n2 = a.count(a[n-1])
    if n1*2 == n:
        print(n//2)
    elif n2*2 == n:
        print(n//2)
    else:
        print(n-n1-n2)

if __name__ == '__main__':
    main()
