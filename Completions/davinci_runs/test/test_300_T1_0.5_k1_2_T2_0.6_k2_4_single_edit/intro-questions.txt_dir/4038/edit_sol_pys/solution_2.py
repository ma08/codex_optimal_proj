

n = int(input())  # number of rows and columns
a = [int(x) for x in input().split()]  # the matrix

if n == 1:  # if there is only one element, it is a magic square
    print('YES')
    print(a[0])
else:
    if len(set(a)) != n*n:  # if there are repeated numbers, it is not a magic square
        print('NO')
    else:
        n1 = n//2  # the number of rows and columns of the matrix
        n2 = n-n1
        a2 = a[n1*n1:n*n]
        a1 = a[0:n1*n1]  # the first half of the matrix
        a1.sort()
        a2.sort()
        a2.reverse()  # the second half of the matrix
        if a1 == a2:  # if the first half and the second half are the same, it is a magic square
            print('YES')
            for i in range(n):
                for j in range(n):
                    print(a[i*n+j],end=' ')
                print()
        else:
            print('NO')
