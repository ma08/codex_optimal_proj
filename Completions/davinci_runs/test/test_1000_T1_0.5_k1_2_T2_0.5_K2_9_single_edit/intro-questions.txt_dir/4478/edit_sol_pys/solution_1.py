import sys
import math
def main():
    k = int(input())
    seqs = []
    for _ in range(k):
        seqs.append([int(x) for x in input().split()])
    sums = []
    for seq in seqs:
        sums.append(sum(seq))
    if k == 2:
        if sums[0] == sums[1]:
            print("YES")
            print("1 1")
            print("2 1")
            sys.exit(0)
        for i in range(len(seqs[0])):
            for j in range(len(seqs[1])):
                if sums[0] + seqs[1][j] - seqs[0][i] == sums[1] + seqs[0][i] - seqs[1][j]:
                    print("YES")
                    print("1 {}".format(i+1))
                    print("2 {}".format(j+1))
                    sys.exit(0)
        print("NO")
        sys.exit(0)
    for i in range(len(seqs)):
        for j in range(i+1, len(seqs)):
            if sums[i] == sums[j]:
                print("YES")
                print("{} 1".format(i+1))
                print("{} 1".format(j+1))
                sys.exit(0)
    for i in range(len(seqs)):
        for j in range(i+1, len(seqs)):
            for k in range(len(seqs[i])):
                for l in range(len(seqs[j])):
                    if sums[i] + seqs[j][l] - seqs[i][k] == sums[j] + seqs[i][k] - seqs[j][l]:
                        print("YES")
                        print("{} {}".format(i+1, k+1))
                        print("{} {}".format(j+1, l+1))
                        sys.exit(0)
    print("NO")

if __name__ == '__main__':
    main()
