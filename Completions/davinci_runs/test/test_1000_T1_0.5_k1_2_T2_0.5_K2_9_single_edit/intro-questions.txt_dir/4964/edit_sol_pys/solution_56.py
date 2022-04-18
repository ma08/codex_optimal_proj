

def main():
    n, h, l = map(int, input().split())  # n: number of movies, h: number of horror movies, l: number of similar movies
    horror = set(map(int, input().split()))
    similar = [[] for _ in range(n)]  # similar[i]: the list of movies similar to movie i
    for _ in range(l):
        a, b = map(int, input().split())
        similar[a].append(b)
        similar[b].append(a)
    horror_index = [0] * n  # horror_index[i]: the number of horror movies in the list of movies similar to movie i
    for i in range(n):
        if i not in horror:
            horror_index[i] = max(horror_index[j] for j in similar[i]) + 1
    print(horror_index.index(max(horror_index)))

main()
