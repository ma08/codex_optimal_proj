

def main():
    n = int(input())
    l = input()
    r = input()

    l_dic = {}
    r_dic = {}
    for i in range(n):
        if l[i] == '?':
            if '?' in l_dic:
                l_dic['?'].append(i+1)
            else:
                l_dic['?'] = [i+1]
        else:
            if l[i] in l_dic:
                l_dic[l[i]].append(i+1)
            else:
                l_dic[l[i]] = [i+1]
        if r[i] == '?':
            if '?' in r_dic:
                r_dic['?'].append(i+1)
            else:
                r_dic['?'] = [i+1]
        else:
            if r[i] in r_dic:
                r_dic[r[i]].append(i+1)
            else:
                r_dic[r[i]] = [i+1]

    res = []
    for i in range(n):
        if l[i] == '?' and r[i] == '?':
            if '?' in l_dic and '?' in r_dic:
                res.append([l_dic['?'].pop(), r_dic['?'].pop()])
            else:
                break
        elif l[i] == '?':
            if r[i] in r_dic:
                res.append([l_dic['?'].pop(), r_dic[r[i]].pop()])
            else:
                break
        elif r[i] == '?':
            if l[i] in l_dic:
                res.append([l_dic[l[i]].pop(), r_dic['?'].pop()])
            else:
                break
        elif l[i] == r[i]:
            if l[i] in l_dic and r[i] in r_dic:
                res.append([l_dic[l[i]].pop(), r_dic[r[i]].pop()])
            else:
                break
        else:
            break

    print(len(res))
    for i in res:
        print(i[0], i[1])


if __name__ == "__main__":
    main()