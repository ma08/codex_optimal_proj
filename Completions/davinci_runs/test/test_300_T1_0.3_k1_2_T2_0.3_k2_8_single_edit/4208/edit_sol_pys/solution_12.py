
import sys

def main():
    n = int(sys.stdin.readline())
    l = sys.stdin.readline().strip().split()
    r = sys.stdin.readline().strip().split()

    l_dict = {}
    r_dict = {}
    for i, v in enumerate(l):
        if v in l_dict:
            l_dict[v].append(i)
        elif v == '?':
            l_dict['?'] = [i]
        elif v not in l_dict:
            l_dict[v] = [i]

    for i, v in enumerate(r):
        if v in r_dict:
            r_dict[v].append(i)
        elif v == '?':
            r_dict['?'] = [i]
        elif v not in r_dict:
            r_dict[v] = [i]

    count = 0
    for k in l_dict:
        if k in r_dict:
            count += min(len(l_dict[k]), len(r_dict[k]))
        elif k == '?':
            count += len(l_dict[k])
    for k in r_dict:
        if k in l_dict:
            count += min(len(l_dict[k]), len(r_dict[k]))
        elif k == '?':
            count += len(r_dict[k])

    print(count)
    for k in l_dict:
        if k in r_dict:
            for i in range(min(len(l_dict[k]), len(r_dict[k]))):
                print(l_dict[k][i] + 1, r_dict[k][i] + 1, sep=' ')
        elif k == '?':
            for i in l_dict[k]:
                print(i + 1, '?', sep=' ')
    for k in r_dict:
        if k in l_dict:
            for i in range(min(len(l_dict[k]), len(r_dict[k]))):
                print(l_dict[k][i] + 1, r_dict[k][i] + 1, sep=' ')
        elif k == '?':
            for i in r_dict[k]:
                print('?', i + 1, sep=' ')


if __name__ == "__main__":
    main()
