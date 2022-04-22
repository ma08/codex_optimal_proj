import sys


def isSorted(sequence):
    return sequence == sorted(sequence)

def read_file(file):
    with open(file, 'r') as f:
        N = int(f.readline())
        sequence = list(map(int, f.readline().split()))
        return sequence


sequence = read_file(sys.argv[1])

if isSorted(sequence):
    print("YES")
else:
    print("NO")
