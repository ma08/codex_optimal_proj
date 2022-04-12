
import sys

def main():
    input_value = sys.stdin.readline()
    input_value = input_value.strip()
    a = int(input_value[0:1])
    b = int(input_value[1:2])
    c = int(input_value[2:3])
    d = int(input_value[3:4])
    for op1 in ["+", "-"]:  # 1番目の演算子
        for op2 in ["+", "-"]:  # 2番目の演算子
            for op3 in ["+", "-"]:  # 3番目の演算子
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:  # 式を評価して7になるか
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7")  # 7になる式を出力
                    break  # ループを抜ける

if __name__ == "__main__":
    main()
