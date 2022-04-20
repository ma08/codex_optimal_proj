

def main():
    n = int(input())
    l = list(input())
    r = list(input())
    l_dict = {}
    r_dict = {}
    for i in range(n):
        if l[i] == '?' and r[i] == '?':
            if '?' in l_dict:
                l_dict['?'].append(i)
            else:
                l_dict['?'] = [i]
            if '?' in r_dict:
                r_dict['?'].append(i)
            else:
                r_dict['?'] = [i]
        elif l[i] == '?':
            if '?' in l_dict:
                l_dict['?'].append(i)
            else:
                l_dict['?'] = [i]
        else:
            if l[i] in l_dict:
                l_dict[l[i]].append(i)
            else:
                l_dict[l[i]] = [i]
        elif r[i] == '?':
            if '?' in r_dict:
                r_dict['?'].append(i)
            else:
                r_dict['?'] = [i]
        else:
            if r[i] in r_dict:
                r_dict[r[i]].append(i)
            else:
                r_dict[r[i]] = [i]
    res = 0
    pairs = []
    for key in l_dict:
        if key in r_dict:
            if len(l_dict[key]) <= len(r_dict[key]):
                res += len(l_dict[key])
                for i in range(len(l_dict[key])):
                    pairs.append([l_dict[key][i]+1, r_dict[key][i]+1])
            else:
                res += len(r_dict[key])
                for i in range(len(r_dict[key])):
                    pairs.append([l_dict[key][i]+1, r_dict[key][i]+1])
    print(res)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    main()
