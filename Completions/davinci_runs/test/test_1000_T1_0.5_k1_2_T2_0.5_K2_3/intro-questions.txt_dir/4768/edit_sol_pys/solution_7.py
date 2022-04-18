

def main():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n - 1):
        for j in range(i + 1, n):
            dna_dict[(i, j)] = hamming_distance(dna[i], dna[j])

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)
def hamming_distance(a, b):
    count = 0
    for i, j in zip(a, b):
        if i != j:
            count += 1
    return count



if __name__ == '__main__':
    main()
