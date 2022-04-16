

import sys

def main():

    n, k = map(int, input().split())
    dna = [input() for _ in range(n)]
    dna_dict = {}

    for i in range(n-1):
        for j in range(i+1, n-1):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()))

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key)


if __name__ == '__main__':
    main()
