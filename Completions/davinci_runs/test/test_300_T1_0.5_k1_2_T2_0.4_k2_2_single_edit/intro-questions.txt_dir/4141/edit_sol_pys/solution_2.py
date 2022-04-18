
num = int(input())
input_list = list(map(int, input().split()))  # inputをsplitしてintに変換してリストに格納

for i in input_list:  # リストの各要素について
    if i % 2 == 0:  # 偶数なら
        if i % 3 != 0 and i % 5 != 0:  # 3でも5でも割り切れないなら
            print("DENIED")
            exit(0)  # 処理を終了
print("APPROVED")
