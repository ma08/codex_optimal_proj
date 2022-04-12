

q = int(input())

for i in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(a)
    
    if k > n or k == 1 or k == n:
        if sum(a) % 2 == 0:
            print("NO")
        else:    
            print("YES")
            if k == 1:
                print(n)
            else:
                for i in range(n):
                    print(i+1, end = " ")
                print()
    else:
        if sum(a) % 2 != 0:
            print("NO")
        else:    
            for i in range(1, n):
                if a[i] % 2 != 0:
                    print("YES")
                    print(i, end = " ")
                    for j in range(2, k+1):
                        print(n-j+2, end = " ")
                    print()
                    break
            else:
                print("NO")
