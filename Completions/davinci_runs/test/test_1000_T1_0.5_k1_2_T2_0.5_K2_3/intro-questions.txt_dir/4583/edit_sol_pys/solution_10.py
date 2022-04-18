import sys

def main():
    input_val = str(sys.stdin.readline())
    input_val = list(input_val.strip())
    a = int(input_val[0])
    b = int(input_val[1])
    c = int(input_val[2])
    d = int(input_val[3])
    # op1を"+"か"-"で決める
    for op1 in ["+", "-"]:
        # op2を"+"か"-"で決める
        for op2 in ["+", "-"]:
            # op3を"+"か"-"で決める
            for op3 in ["+", "-"]:
                # 計算結果が7になるか判定
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:
                    # 計算結果が7になる場合は、その計算式を出力
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7")
                    # breakでループを抜ける
                    break

if __name__ == "__main__":
    main()
