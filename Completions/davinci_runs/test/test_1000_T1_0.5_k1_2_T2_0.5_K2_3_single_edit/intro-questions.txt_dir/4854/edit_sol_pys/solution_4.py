
import sys

def main():
    # read the input, convert to integers
    n, c = int(sys.stdin.readline()), int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    # create a list of lists, flatten the list
    sorted_seq = [item for sublist in sorted(seq) for item in sublist]
    # print the output, separated by spaces
    print(" ".join(map(str, sorted_seq)))

main()
