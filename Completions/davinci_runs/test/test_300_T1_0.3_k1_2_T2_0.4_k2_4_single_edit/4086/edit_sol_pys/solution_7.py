

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a) # set型に変換
    a_dict = {} # 辞書型に変換

    for i in a_set:
        a_dict[i] = a.count(i)

    a_list = [] # リスト型に変換
    for i in a_dict:
        a_list.append(i)

    a_list.sort(key=lambda x: a_dict[x], reverse=True)

    print(len(a_list))
    print(' '.join(map(str, a_list)))

if __name__ == '__main__':
    main()
