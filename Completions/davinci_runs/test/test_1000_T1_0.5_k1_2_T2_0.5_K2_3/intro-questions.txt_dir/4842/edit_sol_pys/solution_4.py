
import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    diff_table = [v]
    while len(diff_table[-1]) > 1: # diff_table[-1] is the last row of diff_table
        diff_table.append([]) # append an empty row
        for i in range(len(diff_table[-2]) - 1): # diff_table[-2] is the second last row of diff_table
            diff_table[-1].append(diff_table[-2][i + 1] - diff_table[-2][i]) # append the difference
    for i in range(len(diff_table)): # print the diff_table
        print("\t".join(map(str, diff_table[i]))) # print each row
    print() # print a new line

def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    print_diff_table(n, v)

if __name__ == '__main__':
    main()
