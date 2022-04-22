


#
# 以下のコードは標準入力と標準出力を用いたサンプルコードです。
# 基本的な入出力方法については、C++入出力奮闘記の方をご覧ください。
#

    """
    文字列を入力して返却します。
    """
def read_line():
    try:
        return input()
    except:
        return None

    """
    空白区切りの整数の入力を一行読み込んで、リストにして返却します。
    """
def read_ints():
    return list(map(int, read_line().split(' ')))

    """
    空白区切りの浮動小数点数の入力を一行読み込んで、リストにして返却します。
    """
def read_floats():
    return list(map(float, read_line().split(' ')))


    """
    標準入力から読み込んだ整数です。
    """
def main():

    T, X = read_ints()
    print(T / X)


if __name__ == '__main__':
    main()
