

import sys

def main():
    N, C = sys.stdin.readline().split()
    N = int(N)
    C = int(C)
    seq = sys.stdin.readline().split()
    for i in range(N):
        seq[i] = int(seq[i])
    counts = {}
    for i in range(N):
        if seq[i] not in counts:
            counts[seq[i]] = 1
        else:
            counts[seq[i]] += 1
    sorted_counts = sorted(counts.items(), key=lambda tup: tup[1], reverse=True)
    sorted_seq = []
    for i in range(len(sorted_counts)):
        sorted_seq.append([])
        for j in range(N):
            if seq[j] == sorted_counts[i][0]:
                sorted_seq[i].append(seq[j])
    sorted_seq = [item for sublist in sorted_seq for item in sublist]
    for i in range(N):
        print(sorted_seq[i], end=" ")
    print("")

main()
