

import sys

def main():
    n = int(input())
    dna = [input() for _ in range(n)]
    edges = []  # list of edges
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, hamming(dna[i], dna[j])))
    edges.sort(key=lambda x: x[2])  # sort edges by distance
    components = {i: i for i in range(n)}
    total_distance = 0  # total distance of MST
    for i, j, d in edges:
        if components[i] != components[j]:  # if not in the same component
            total_distance += d
            c1 = components[i]  # component of i
            c2 = components[j]  # component of j
            for k in range(n):
                if components[k] == c2:
                    components[k] = c1  # merge components
    print(total_distance)
    for i, j, d in edges: 
        if components[i] != components[j]: 
            print(i, j) 

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main()
