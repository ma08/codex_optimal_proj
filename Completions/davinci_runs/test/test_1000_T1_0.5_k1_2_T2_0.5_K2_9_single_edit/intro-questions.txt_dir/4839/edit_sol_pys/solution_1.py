

n = int(input())
c = [int(x) for x in input().split()]

c.sort()

if c[-1] > n:
    print("impossible")
else:
    m = 0
    for i in range(n-1, -1, -1):
        if c[i] > m + 1:  #if the last element is greater than the number of elements
            m += 1
        else:
            break
    print(m/n)
