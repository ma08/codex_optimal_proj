# abc068_b.py

# from https://qiita.com/kazeto/items/1d902c7b2a2af0d7f8b8
def read_line(): # 標準入力から一行読み込む
    try:
        line = input()
        return line
    except:
        return None

def read_ints(): # 標準入力から整数リストを読み込む
    return list(map(int, read_line().split(' ')))

def read_floats(): # 標準入力から実数リストを読み込む
    return list(map(float, read_line().split(' ')))

def main():
    T, X = read_ints()
    print(T / X)

if __name__ == '__main__':
    main()
