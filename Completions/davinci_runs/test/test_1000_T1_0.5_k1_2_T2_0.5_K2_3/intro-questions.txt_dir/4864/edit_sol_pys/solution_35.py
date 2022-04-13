

def main():
    R, C, Zr, Zc = [int(i) for i in input().split()] # R:行数 C:列数 Zr:行の倍率 Zc:列の倍率
    article = [input() for _ in range(R)] # 記事を読み込む
    for i in range(R): # 行数分ループ
        for j in range(Zr): # 行の倍率分ループ
            new_line = '' # 新しい行の文字列を空にする
            for k in range(C): # 列数分ループ
                for l in range(Zc): # 列の倍率分ループ
                    new_line += article[i][k] # 新しい行の文字列に記事の文字を追加する
            print(new_line) # 新しい行を出力する


if __name__ == '__main__':
    main()
