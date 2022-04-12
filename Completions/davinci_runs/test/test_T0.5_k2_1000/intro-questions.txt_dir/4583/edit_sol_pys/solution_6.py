import sys

def main():
    input_val = str(sys.stdin.readline()).strip()
    a = int(input_val[0:1])
    b = int(input_val[1:2])
    c = int(input_val[2:3])
    d = int(input_val[3:4])
    for op1 in ["+", "-"]:  # 1
        for op2 in ["+", "-"]:  # 2
            for op3 in ["+", "-"]:  # 3
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:  # 4
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7")  # 5
                    exit()

if __name__ == "__main__":
    main()
