

q = int(input())

for i in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(a)
    
    if k > n:
        print("NO")
        continue
    
    if k == 1:
        summ = sum(a)
        if summ % 2 == 0:
            print("NO")
        else:
            print("YES")
            print(n)
        continue
    
    # if k == n:
    #     summ = sum(a)
    #     if summ % 2 == 0:
    #         print("NO")
    #     else:
    #         print("YES")
    #         for i in range(n):
    #             print(i+1, end = " ")
    #         print()
    #     continue
    
    if k == 2:
        summ = sum(a)
        if summ % 2 != 0:
            print("NO")
            continue
        else:
            for i in range(1, n):
                if a[i] % 2 != 0:
                    print("YES")
                    print(i, end = " ")
                    print(n)
                    break
            else:
                print("NO")
            continue
    
    if k > 2:
        summ = sum(a)
        if summ % 2 != 0:
            print("NO")
            continue
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
            continue
