

def main():
    n, k = map(int, input().split())
    dna = [input() for _ in range(n)]
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            edges.append((i, j, hamming(dna[i], dna[j])))
    edges.sort(key=lambda x: x[2])
    components = {i: i for i in range(n - 1)}
    total_distance = 0
    for i, j, d in edges:
        if components[i] != components[j]:
            total_distance += d
            c1 = components[i]
            c2 = components[j]
            for k in range(n - 1):
                if components[k] == c2:
                    components[k] = c1
    print(total_distance)
    for i, j, d in edges:
        if components[i] != components[j]:
            print(i, j)
            c1 = components[i]
            c2 = components[j]
            for k in range(n - 1):
                if components[k] == c2:
                    components[k] = c1

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main()
