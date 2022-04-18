
import sys

def main():
    input_val = str(sys.stdin.readline())
    input_val = list(input_val.strip())
    a = int(input_val[0])
    b = int(input_val[1])
    c = int(input_val[2])
    d = int(input_val[3])
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7")
                    sys.exit()

if __name__ == "__main__":
    main()
