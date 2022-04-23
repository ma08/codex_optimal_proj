

import sys

def main():
    n = sys.stdin.readline()
    names = []
    for line in sys.stdin:
        names.append(line.strip())
    print(get_num_triples(names) % ((10**9) + 7))

def get_num_triples(names):
    names_with_m = [name for name in names if name[0] == 'M' or name[0] == 'm']
    names_with_a = [name for name in names if name[0] == 'A' or name[0] == 'a']
    names_with_r = [name for name in names if name[0] == 'R' or name[0] == 'r']
    names_with_c = [name for name in names if name[0] == 'C' or name[0] == 'c']
    names_with_h = [name for name in names if name[0] == 'H' or name[0] == 'h']
    num_triples = 0
    num_triples += len(names_with_m) * len(names_with_a) * len(names_with_r)
    num_triples += len(names_with_m) * len(names_with_a) * len(names_with_c)
    num_triples += len(names_with_m) * len(names_with_a) * len(names_with_h)
    num_triples += len(names_with_m) * len(names_with_r) * len(names_with_c)
    num_triples += len(names_with_m) * len(names_with_r) * len(names_with_h)
    num_triples += len(names_with_m) * len(names_with_c) * len(names_with_h)
    num_triples += len(names_with_a) * len(names_with_r) * len(names_with_c)
    num_triples += len(names_with_a) * len(names_with_r) * len(names_with_h)
    num_triples += len(names_with_a) * len(names_with_c) * len(names_with_h)
    num_triples += len(names_with_r) * len(names_with_c) * len(names_with_h)
    return num_triples

if __name__ == '__main__':
    main()
