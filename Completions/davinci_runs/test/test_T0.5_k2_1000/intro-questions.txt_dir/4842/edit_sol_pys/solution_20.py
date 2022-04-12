import sys

def print_diff_table(n, v):
    diff_table = [v] # diff_table[0] = v
    while len(diff_table[-1]) > 1: # diff_table[-1] = diff_table[-2]
        diff_table.append([]) # diff_table[-1] = []
        for i in range(len(diff_table[-2]) - 1): # diff_table[-2] = diff_table[-3]
            diff_table[-1].append(diff_table[-2][i + 1] - diff_table[-2][i]) # diff_table[-1] = diff_table[-2][i + 1] - diff_table[-2][i]
    for i in range(len(diff_table)): # diff_table[i]
        print("\t".join(map(str, diff_table[i]))) # diff_table[i]
    print() # print()

def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    print_diff_table(n, v)

if __name__ == '__main__':
    main()
