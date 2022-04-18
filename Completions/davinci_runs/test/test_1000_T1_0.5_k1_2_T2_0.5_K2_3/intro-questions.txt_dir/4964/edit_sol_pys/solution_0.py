

def main():
    n, h, l = map(int, input().split())
    hore = set(map(int, input().split())) - {0}
    similar = [[] for _ in range(n + 1)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b + 1)
        similar[b + 1].append(a)
    hore_index = [0] * (n + 1)
    for i in range(1, n + 1):
        if i not in hore and hore_index[i] == 0:
            hore_index[i] = max(hore_index[j] for j in similar[i]) + 1
    print(hore_index.index(max(hore_index)))

main()
