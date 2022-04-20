

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)  # 出現する数字のみを集めたset
    a_dict = {}

    for i in a_set:  # setから順番に要素を取り出し、その値をkeyとして、その値の出現回数をvalueとして辞書に追加
        a_dict[i] = a.count(i)

    a_list = []  # 出現回数順にソートしたいので、辞書のkeyをlistに追加
    for i in a_dict:  # 辞書のkeyを順番に取り出し、それをlistに追加
        a_list.append(i)

    a_list.sort(key=lambda x: a_dict[x], reverse=True)  # 出現回数順にソート

    print(len(a_list))
    print(' '.join(map(str, a_list)))

if __name__ == '__main__':
    main()
