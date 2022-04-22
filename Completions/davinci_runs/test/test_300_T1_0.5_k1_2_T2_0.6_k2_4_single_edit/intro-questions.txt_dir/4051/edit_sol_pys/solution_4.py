

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
        print(a)

def bubble_sort(a):
    n = len(a)
    flag = True
    while flag:
        flag = False
        for j in range(n-1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                flag = True
        print(a)

def selection_sort(a):
    n = len(a)
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
        print(a)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(*a)
    #insertion_sort(a)
    #bubble_sort(a)
    #selection_sort(a)

main()
