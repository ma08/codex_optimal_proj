
import sys

def main():
    n = int(sys.stdin.readline())
    l = list(sys.stdin.readline().strip())
    r = list(sys.stdin.readline().strip())

    l_dict = {}
    r_dict = {}
    for i in range(n):
        if l[i] == '?':
            if '?' in l_dict:
                l_dict['?'].append(i)
            else:
                l_dict['?'] = [i]
        else:
            if l[i] in l_dict:
                l_dict[l[i]].append(i)
            else:
                l_dict[l[i]] = [i]

        if r[i] == '?':
            if '?' in r_dict:
                r_dict['?'].append(i)
            else:
                r_dict['?'] = [i]
        else:
            if r[i] in r_dict:
                r_dict[r[i]].append(i)
            else:
                r_dict[r[i]] = [i]

    count = 0
    for k, v in l_dict.items():
        if k == '?':
            count += len(v)
        else:
            if k in r_dict:
                count += min(len(v), len(r_dict[k]))
    for k, v in r_dict.items():
        if k == '?':
            count += len(v)
        else:
            if k in l_dict:
                count += min(len(v), len(l_dict[k]))

    print(count)
    for i in range(n):
        if l[i] == '?' and r[i] == '?':
            l[i] = 'a'
            r[i] = 'a'
        elif l[i] == '?':
            l[i] = r[i]
        elif r[i] == '?':
            r[i] = l[i]

    print(''.join(l))
    print(''.join(r))


if __name__ == "__main__":
    main()
