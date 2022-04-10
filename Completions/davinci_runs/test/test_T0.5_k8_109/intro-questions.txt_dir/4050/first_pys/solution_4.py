

def find_blocks(a):
    n = len(a)
    k = 1
    l = [1] * n
    r = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if a[i] == a[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
                r[i] = j
        if l[i] > l[k]:
            k = i
    print(l[k])
    while k >= 0:
        print(k+1, r[k]+1)
        k = r[k]

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    find_blocks(a)