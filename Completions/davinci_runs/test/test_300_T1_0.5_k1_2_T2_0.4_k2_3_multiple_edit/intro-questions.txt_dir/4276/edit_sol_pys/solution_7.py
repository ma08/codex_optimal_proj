
N = int(input())
a = list(map(int, input().split()))

def bubbleSort(a):
    for i in range(N):
        for j in range(N-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                print(*a)

bubbleSort(a)
