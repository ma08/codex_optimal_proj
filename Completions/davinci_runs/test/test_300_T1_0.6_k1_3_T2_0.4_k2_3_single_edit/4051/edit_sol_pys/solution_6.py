
#-----Solution-----

def ravioli_sort(n,a):
    for i in range(n-1):
        if a[i] > a[i+1] and a[i] - a[i+1] >= 2:
            return 'NO'
    return 'YES'

n = int(input())
a = list(map(int,input().split()))
print(ravioli_sort(n,a))
