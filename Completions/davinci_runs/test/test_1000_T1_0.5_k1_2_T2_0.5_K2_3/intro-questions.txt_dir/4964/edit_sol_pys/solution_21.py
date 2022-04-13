# def main():
#     n, m, k = map(int, input().split())
#     a = [int(input()) for _ in range(n)]
#     b = [int(input()) for _ in range(m)]
#     a.sort()
#     b.sort()


def main():
    n, h, l = map(int, input().split())
    horror = set(map(int, input().split()))
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    horror_index = [0] * n
    for i in range(n):
        if i not in horror:
            horror_index[i] = max(horror_index[j] for j in similar[i]) + 1
    print(horror_index.index(max(horror_index)))

main()
