

import sys

def main():
    input_val = str(sys.stdin.readline())
    input_val = list(input_val.strip())
    a, b, c, d = int(input_val[0]), int(input_val[1]), int(input_val[2]), int(input_val[3])
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                problem = str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)
                if eval(problem) == 7:
                    print(problem + "=7")
                    break

if __name__ == "__main__":
    main()
