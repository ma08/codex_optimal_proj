

def main():
    n = int(input())
    l = input().split()
    r = input().split()
    l_dict = {}
    r_dict = {}
    for i in range(n):
        if l[i] == '?' or r[i] == '?':
            if '?' in l_dict:
                l_dict['?'].append(i+1)
            else:
                l_dict['?'] = [i+1]
        else:
            if l[i] in l_dict:
                l_dict[l[i]].append(i+1)
            else:
                l_dict[l[i]] = [i+1]
    res = 0
    pairs = []
    for key in l_dict:
        if key in r_dict:
            if len(l_dict[key]) <= len(r_dict[key]):
                res += len(l_dict[key])
                for i in range(len(l_dict[key])):
                    pairs.append([l_dict[key][i], r_dict[key][i]])
            else:
                res += len(r_dict[key])
                for i in range(len(r_dict[key])):
                    pairs.append([l_dict[key][i], r_dict[key][i]])
    if '?' in l_dict and '?' in r_dict:
        res += min(len(l_dict['?']), len(r_dict['?']))
        for i in range(min(len(l_dict['?']), len(r_dict['?']))):
            pairs.append([l_dict['?'][i], r_dict['?'][i]])
    print(res)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    main()
