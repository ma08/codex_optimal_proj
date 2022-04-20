# coding: utf-8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)
    a_dict = {}

    for i in a_set:
        a_dict[i] = a.count(i)

    a_list = []
    for i in a_dict:
        a_list.append(i)

    a_list.sort(key=lambda x: a_dict[x], reverse=True)

    print(len(a_list))
    print(' '.join(map(str, a_list)))

if __name__ == '__main__':
    main()
