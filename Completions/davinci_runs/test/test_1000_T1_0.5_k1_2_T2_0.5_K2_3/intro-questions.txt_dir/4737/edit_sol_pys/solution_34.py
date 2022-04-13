# coding: utf-8

def main():
    n, p = map(int, input().split())  # 選手数, 先頭の選手番号
    times = list(map(int, input().split()))  # 時間
    times = times[p:] + times[:p]  # 先頭の選手を先頭に移動
    max_solved = 0  # 解いた問題数
    min_penalty = 0  # ペナルティ
    remaining = 300  # 残り時間
    for t in times:  # 各選手の時間
        if remaining >= t:  # 残り時間が十分ある場合
            remaining -= t  # 残り時間から解いた時間を引く
            max_solved += 1  # 解いた問題数を1増やす
            min_penalty += t  # ペナルティに解いた時間を加える
        else:  # 残り時間が足りない場合
            break  # 終了
    print(max_solved, min_penalty)  # 最大解いた問題数とペナルティを出力

if __name__ == "__main__":
    main()
