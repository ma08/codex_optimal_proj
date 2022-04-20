

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)  # set型を使用して重複を削除する
    a_dict = {}  # 空の辞書型を定義

    for i in a_set:  # set型の要素を辞書型のkeyにし、出現回数をvalueにする
        a_dict[i] = a.count(i)

    a_list = []
    for i in a_dict:
        a_list.append(i)

    a_list.sort(key=lambda x: a_dict[x], reverse=True)

    print(len(a_list))
    print(' '.join(map(str, a_list)))

if __name__ == '__main__':
    main()
