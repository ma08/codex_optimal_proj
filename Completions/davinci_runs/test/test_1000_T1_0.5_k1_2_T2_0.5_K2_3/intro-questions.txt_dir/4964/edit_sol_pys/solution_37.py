

def main():
    n, h, l = map(int, input().split())
    hore = set(map(int, input().split()))
    similar = [[] for i in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    hore_index = [0] * n
    for i in range(n):
        if i not in hore:
            hore_index[i] = max(hore_index[j] for j in similar[i]) + 1
    print(hore_index.index(max(hore_index)))

main()
