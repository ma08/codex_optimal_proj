import sys

def main():
    input_val = list(sys.stdin.readline().strip())
    a, b, c, d = int(input_val[0]), int(input_val[1]), int(input_val[2]), int(input_val[3])
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7")
                    break

if __name__ == "__main__":
    main()
