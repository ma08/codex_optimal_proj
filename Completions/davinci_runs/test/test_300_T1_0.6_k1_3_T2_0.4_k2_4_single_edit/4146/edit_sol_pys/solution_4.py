

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    n1 = a.count(a[0])
    n2 = a.count(a[-1])
    if n1 == n:
        print(0)
    elif n1*2 == n:
        print(n//2-1)
    elif n2 == n:
        print(0)
    elif n2*2 == n and n2 != 1:
        print(n//2-1)
    else:
        print(n-n1-n2)

if __name__ == '__main__':
    main()
