

def main(n, k, dna):
    components = {i: i for i in range(n)}
    total_distance = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if components[i] != components[j]:
                d = hamming(dna[i], dna[j])
                if d < total_distance:
                    total_distance = d
                    c1 = components[i]
                    c2 = components[j]
                    for k in range(n):
                        if components[k] == c2:
                            components[k] = c1
    return total_distance

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main(6, 5, ["CCTAA", "CTAAA", "TAAAA", "AAATT", "AATTT", "TTTTT"])
