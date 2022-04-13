

def get_min_dif(string):
    min_dif = 1001  # 初期値を大きな値に設定
    for i in range(len(string) - 2):
        dif = abs(753 - int(string[i:i+3]))  # 3桁の数を取り出して、753との差を算出
        if dif < min_dif:
            min_dif = dif
    return min_dif  # 最小値を返す

if __name__ == '__main__':
    string = input()
    print(get_min_dif(string))
