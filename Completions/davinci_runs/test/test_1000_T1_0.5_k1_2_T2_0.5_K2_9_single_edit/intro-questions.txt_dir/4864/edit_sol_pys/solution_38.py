

def main():
    R, C, Zr, Zc = [int(i) for i in input().split()]  # R:行数 C:列数 Zr:行方向の伸縮率 Zc:列方向の伸縮率
    article = [input() for i in range(R)]  # 入力

    for i in range(R):
        for j in range(Zr):
            new_line = ''  # 伸縮した行を保存する変数
            # 伸縮する
            for k in range(C):
                for l in range(Zc):
                    new_line += article[i][k]
            print(new_line)  # 出力

if __name__ == '__main__':
    main()
