# https://atcoder.jp/contests/abc136/tasks/abc136_d


def main():
    n = int(input())
    s = input()
    s_dict = {i: 0 for i in range(n)}
    for i in range(n):
        s_dict[i] = s[i]
    s_dict = sorted(s_dict.items(), key=lambda x: x[1])
    s_dict_r = dict()
    for i in s_dict:
        s_dict_r[i[0]] = i[1]
    d = 0
    while s_dict_r != dict():
        d += 1
        for j in s_dict_r:
            if s_dict_r[j] == 'R':
                s_dict_r[j] = 'L'
                s_dict_r[j-1] = 'R'
            elif s_dict_r[j] == 'L':
                s_dict_r[j] = 'R'
                s_dict_r[j-1] = 'L'
    print(d)


if __name__ == '__main__':
    main()
