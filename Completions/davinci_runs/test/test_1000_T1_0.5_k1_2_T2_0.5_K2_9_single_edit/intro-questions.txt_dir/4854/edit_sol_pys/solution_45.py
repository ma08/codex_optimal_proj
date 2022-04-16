

import sys

def main():
    # read the input
    N = sys.stdin.readline().split()
    N = int(N)
    seq = sys.stdin.readline().split()
    # convert to integers
    for i in range(N):
        seq[i] = int(seq[i])
    # create a dictionary of counts
    counts = {}
    for i in range(N):
        if seq[i] not in counts:
            counts[seq[i]] = 1
        else:
            counts[seq[i]] += 1
    # sort the dictionary by value
    sorted_counts = sorted(counts.items(), key=lambda tup: tup[1], reverse=True)
    # create a list of lists
    sorted_seq = []
    for i in range(len(sorted_counts)):
        sorted_seq.append([])
        for j in range(N):
            if seq[j] == sorted_counts[i][0]:
                sorted_seq[i].append(seq[j])
    # flatten the list
    sorted_seq = [item for sublist in sorted_seq for item in sublist]
    # print the output
    for i in range(N):
        print(sorted_seq[i], end=" ")
    print("")

main()
