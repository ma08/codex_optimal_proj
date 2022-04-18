import sys

def main():
    input_val = str(sys.stdin.readline()).strip()
    input_val = list(input_val)
    a = int(input_val[0])
    b = int(input_val[1])
    c = int(input_val[2])
    d = int(input_val[3])
    for op1 in ["+", "-"]: # op1を"+"か"-"で決める
        for op2 in ["+", "-"]: # op2を"+"か"-"で決める
            for op3 in ["+", "-"]: # op3を"+"か"-"で決める
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7: # 計算結果が7になるか判定
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7") # 計算結果が7になる場合は、その計算式を出力
                    break # breakでループを抜ける

if __name__ == "__main__":
    main()
