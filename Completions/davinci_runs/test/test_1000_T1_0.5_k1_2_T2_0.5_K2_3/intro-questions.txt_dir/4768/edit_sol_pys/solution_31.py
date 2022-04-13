

def main():
    n = int(input())
    dna = [input() for _ in range(n)]
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, hamming(dna[i], dna[j])))
    edges.sort(key=lambda x: x[2])
    components = {i: i for i in range(n)}
    total_distance = 0
    for i, j, d in edges:
        if components[i] != components[j]:
            total_distance += d
            c1 = components[i]
            c2 = components[j]
            for k in range(n):
                if components[k] == c2:
                    components[k] = c1
    print(total_distance)

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main()
