

#-----Solution-----

def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n
    a = a[-k:] + a[:-k]
    return [a[i] for i in queries]

n,k,q = map(int, input().split())
a = list(map(int, input().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
result = circularArrayRotation(a, k, queries)
print('\n'.join(map(str, result)))
