

def main():
    n, h, l = map(int, input().split())
    horror_movies = set(map(int, input().split())) - 1
    similar = [[] for _ in range(n)]
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    horror_index = [0] * (n + 1)
    for i in range(n):
        horror_index[i + 1] = max(horror_index[j] for j in similar[i]) + 1 if i + 1 not in horror_movies else 0
    print(horror_index.index(max(horror_index)))

main()
