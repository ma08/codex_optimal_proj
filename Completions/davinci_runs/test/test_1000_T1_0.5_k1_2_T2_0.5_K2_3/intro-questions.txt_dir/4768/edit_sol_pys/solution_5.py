

def main():

    n, k = map(int, input().split())
    dna = []
    for i in range(n):
        dna.append(input())
    dna_dict = {}

    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(key[0] + 1, key[1] + 1)


if __name__ == '__main__':
    main()
