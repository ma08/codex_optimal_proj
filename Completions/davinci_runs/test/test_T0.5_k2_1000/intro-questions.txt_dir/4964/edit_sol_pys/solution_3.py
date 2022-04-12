

def main():
    n, h, l = map(int, input().split())
    horror_movies = set(map(int, input().split())) - 1
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a - 1].append(b - 1)
        similar[b - 1].append(a - 1)
    horror_index = [0] * n
    for i in range(n):
        if i not in horror_movies:
            horror_index[i] = max(horror_index[j] for j in similar[i]) + 1
    print(horror_index.index(max(horror_index)))

main()
