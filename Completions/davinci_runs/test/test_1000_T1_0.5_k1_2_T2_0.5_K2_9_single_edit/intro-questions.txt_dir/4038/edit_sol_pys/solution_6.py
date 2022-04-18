

def is_magic_square(a):
    n = len(a)
    if n == 1:
        return True
    if len(set(a)) != n*n:
        return False
    else:
        n1 = n//2
        n2 = n-n1
        a2 = a[n1*n1:n*n]
        a1 = a[0:n1*n1]
        a1.sort()
        a2.sort()
        a2.reverse()
        if a1 == a2:
            return True
        else:
            return False

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if is_magic_square(a):
        print('YES')
        for i in range(n):
            for j in range(n):
                print(a[i*n+j],end=' ')
            print()
    else:
        print('NO')

if __name__ == "__main__":
    main()
