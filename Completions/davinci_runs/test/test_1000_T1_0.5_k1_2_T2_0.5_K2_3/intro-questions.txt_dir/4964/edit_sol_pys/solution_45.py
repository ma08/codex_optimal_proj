

def main():
    n, h, l = map(int, input().split())
    hore = set(map(int, input().split())) - {0}
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a - 1].append(b - 1)
        similar[b - 1].append(a - 1)
    hore_index = [0] * n
    for i in range(n):
        if i not in hore and similar[i]:
            hore_index[i] = max(hore_index[j] for j in similar[i]) + 1
    print(hore_index.index(max(hore_index)) + 1)

main()
