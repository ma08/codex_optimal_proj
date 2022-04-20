

# from https://qiita.com/kazetof/items/1d902c7b2a2af0d7f8b8 
# 入力を行ごとに受け取る
def read_line():
    try:
        return input()
    except:
        return None

# 文字列を空白区切りのリストに変換
def read_ints(): 
    return list(map(int, read_line().split(' ')))

def read_floats(): 
    return list(map(float, read_line().split(' ')))

def main(): 
    T, X = read_ints()
    print(T / X)

if __name__ == '__main__':
    main()
