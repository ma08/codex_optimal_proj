

def count(n):
    arr=[]
    for i in range(n):
        arr.append(i)
    return arr

n, k = map(int, input().split())
print(count(n, k))
