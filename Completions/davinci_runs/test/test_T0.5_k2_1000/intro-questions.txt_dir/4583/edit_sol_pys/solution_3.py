
import sys

def main():
    input_val = list(str(sys.stdin.readline()).strip())
    a = input_val[0]
    b = input_val[1]
    c = input_val[2]
    d = input_val[3]
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                if eval(a + op1 + b + op2 + c + op3 + d) == 7:
                    print(a + op1 + b + op2 + c + op3 + d + "=7")
                    break

if __name__ == "__main__":
    main()
