
def main():
    n, h, l = map(int, input().split())
    holy = set(map(int, input().split()))
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    holy_index = [0] * n
    for i in range(n):
        if i not in holy:
            holy_index[i] = max(holy_index[j] for j in similar[i]) + 1
    print(holy_index.index(max(holy_index)))

main()
