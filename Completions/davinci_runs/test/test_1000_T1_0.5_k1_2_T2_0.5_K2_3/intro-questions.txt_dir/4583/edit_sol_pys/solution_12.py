import sys

def main():
    input_val = list(sys.stdin.readline().strip())
    a = int(input_val[0]) # aを1文字目で決める
    b = int(input_val[1]) # bを2文字目で決める
    c = int(input_val[2]) # cを3文字目で決める
    d = int(input_val[3]) # dを4文字目で決める

    for op1 in ["+", "-"]: # op1を"+"か"-"で決める(ここでは、op1を"+"と"-"(つまり、2通り)で決める)
        for op2 in ["+", "-"]: # op2を"+"か"-"で決める(ここでは、op2を"+"と"-"(つまり、2通り)で決める)
            for op3 in ["+", "-"]: # op3を"+"か"-"で決める(ここでは、op3を"+"と"-"(つまり、2通り)で決める)
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7: # 計算結果が7になるか判定(ここでは、計算結果が7になるか判定する)
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7") # 計算結果が7になる場合は、その計算式を出力(ここでは、計算結果が7になる場合は、その計算式を出力する)
                    break # breakでループを抜ける(ここでは、breakでループを抜ける)

if __name__ == "__main__":
    main()
