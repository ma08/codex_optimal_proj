

import numpy as np

def main():
    n, b, a = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()] # 入力を配列に格納
    s = np.array(s)
    b_now, a_now = b, a # 初期値を設定
    i = 0
    while i < n:
        if s[i] == 1: # ソーラーパネルが1なら
            if a_now < a: # バッテリーが残っていれば
                a_now += 1
            else: # バッテリーが残っていなければ
                b_now += 1
            i += 1
        elif s[i] == 0:
            if b_now > 0:
                b_now -= 1
                i += 1
            elif a_now > 0:
                a_now -= 1
                i += 1
            else:
                break
    print(i)

if __name__ == "__main__":
    main()
