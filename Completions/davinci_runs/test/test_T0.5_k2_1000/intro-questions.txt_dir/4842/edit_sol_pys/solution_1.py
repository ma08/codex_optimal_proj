
import sys

def print_diff_table(n, values):
    diff_tables = [values]
    while len(diff_tables[-1]) > 1:
        diff_tables.append([])
        for i in range(len(diff_tables[-2]) - 1):
            diff_tables[-1].append(diff_tables[-2][i + 1] - diff_tables[-2][i])
    for i in range(len(diff_tables)):
        print("\t".join(map(str, diff_tables[i])))
    print()


def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    print_diff_table(n, v)


if __name__ == '__main__':
    main()
