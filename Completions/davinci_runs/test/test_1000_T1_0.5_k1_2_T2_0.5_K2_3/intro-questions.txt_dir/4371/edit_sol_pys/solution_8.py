

def get_min_dif(string):
    min_dif = 1001
    for i in range(len(string) - 2):  # 要素数-2まで
        dif = abs(753 - int(string[i:i+3]))  # i番目からi+3番目までの文字列を数値に変換
        if dif < min_dif:
            min_dif = dif
    return min_dif

if __name__ == '__main__':
    string = input()
    print(get_min_dif(string))
