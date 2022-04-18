
import sys

def main():
    input_value = str(sys.stdin.readline())
    input_value = list(input_value.strip())
    a = int(input_value[0])
    b = int(input_value[1])
    c = int(input_value[2])
    d = int(input_value[3])
    for op1 in ["+", "-"]:
        for op2 in ["+", "-"]:
            for op3 in ["+", "-"]:
                if eval(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d)) == 7:
                    print(str(a) + op1 + str(b) + op2 + str(c) + op3 + str(d) + "=7") 
                    break

if __name__ == "__main__":
    main()
