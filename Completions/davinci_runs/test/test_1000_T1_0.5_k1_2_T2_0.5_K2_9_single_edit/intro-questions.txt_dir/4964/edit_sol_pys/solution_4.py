

    import sys
    sys.setrecursionlimit(10**6)
def main():
    n, h, l = map(int, input().split())
    horror = set(map(int, input().split()))
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    horror_index = [-1] * n
    for i in horror:
        horror_index[i] = 0
    for i in range(n):  # i is not horror
        if horror_index[i] == -1:
            horror_index[i] = dfs(i, similar, horror_index)
    print(horror_index.index(max(horror_index)))  # index of max


def dfs(i, similar, horror_index):
    if horror_index[i] != -1:
        return horror_index[i]
    horror_index[i] = max(dfs(j, similar, horror_index) for j in similar[i]) + 1
    return horror_index[i]


main()
