

def main():
    n = int(input())
    l = input().split()
    r = input().split()
    l_dict = {}
    r_dict = {}
    for i in range(n):
        if l[i] == '?':  # if the character is ?
            if '?' in l_dict:
                l_dict['?'].append(i)
            else:
                l_dict['?'] = [i]
        else:  # if the character is not ?
            if l[i] in l_dict:
                l_dict[l[i]].append(i)
            else:
                l_dict[l[i]] = [i]
        if r[i] == '?':  # if the character is ?
            if '?' in r_dict:
                r_dict['?'].append(i)
            else:
                r_dict['?'] = [i]
        else:  # if the character is not ?
            if r[i] in r_dict:
                r_dict[r[i]].append(i)
            else:
                r_dict[r[i]] = [i]
    res = 0
    pairs = []
    for key in l_dict:  # for every key in l_dict
        if key in r_dict:
            if len(l_dict[key]) <= len(r_dict[key]):  # if the length of the list is less than or equal to the length of the list in r_dict
                res += len(l_dict[key])
                for i in range(len(l_dict[key])):  # for every index in the list
                    pairs.append([l_dict[key][i]+1, r_dict[key][i]+1])
            else:  # if the length of the list is greater than the length of the list in r_dict
                res += len(r_dict[key])
                for i in range(len(r_dict[key])):
                    pairs.append([l_dict[key][i]+1, r_dict[key][i]+1])
    if '?' in l_dict and '?' in r_dict:
        res += min(len(l_dict['?']), len(r_dict['?']))
        for i in range(min(len(l_dict['?']), len(r_dict['?']))):
            pairs.append([l_dict['?'][i]+1, r_dict['?'][i]+1])
    print(res)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    main()
