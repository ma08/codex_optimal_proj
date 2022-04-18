import math
import sys

def main(n, k, dna):
    components = {i: i for i in range(1, n + 1)}
    total_distance = float('inf')
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if components[i] != components[j]:
                d = hamming(dna[i - 1], dna[j - 1])
                if d < total_distance:
                    total_distance = d
                    c1 = components[i]
                    c2 = components[j]
                    for k in range(1, n + 1):
                        if components[k] == c2:
                            components[k] = c1
    return total_distance

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main()
