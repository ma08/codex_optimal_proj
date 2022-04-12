

def main():
    n = int(input())
    dna = [input() for _ in range(n)]
    total_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_distance += hamming(dna[i], dna[j])
    print(total_distance)
    for i in range(n):
        for j in range(i + 1, n):
            print(i, j)

def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))

main()
