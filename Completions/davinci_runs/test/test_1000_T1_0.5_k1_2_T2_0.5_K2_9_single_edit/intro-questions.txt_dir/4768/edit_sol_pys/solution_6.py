#!/usr/bin/env python3

import sys

def main():

    n, k = map(int, input().split())
    dna = [input() for i in range(n)]
    dna_dict = {}

    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for x in range(k):
                if dna[i][x] != dna[j][x]:
                    count += 1
            dna_dict[(i,j)] = count

    print(min(dna_dict.values()), end='\n')

    for key, value in dna_dict.items():
        if value == min(dna_dict.values()):
            print(*key, end=' ')


if __name__ == '__main__':
    main()
