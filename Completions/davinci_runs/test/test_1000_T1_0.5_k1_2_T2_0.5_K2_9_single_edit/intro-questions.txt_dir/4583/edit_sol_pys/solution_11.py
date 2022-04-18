

import sys

def main():
    input_val = str(sys.stdin.readline())
    input_val = list(input_val.strip())
    a = int(input_val[0])
    b = int(input_val[1])
    c = int(input_val[2])
    d = int(input_val[3])
    for op1 in ["+", "-"]: # 1つ目の計算
        for op2 in ["+", "-"]: # 2つ目の計算
            for op3 in ["+", "-"]: # 3つ目の計算
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7: # 計算式が7になるかどうかを判定
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7") # 7になった場合に出力
                    exit() # 出力したら終了

if __name__ == "__main__":
    main()
