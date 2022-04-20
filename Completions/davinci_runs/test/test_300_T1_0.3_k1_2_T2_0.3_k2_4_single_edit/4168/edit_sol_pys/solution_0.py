

import sys

def main():
    input_num = int(sys.stdin.readline())
    output_str = ""
    while input_num != 0:
        if input_num % 2 == 0:
            output_str = "0" + output_str
            input_num //= -2
        else:
            output_str = "1" + output_str
            input_num = (input_num - 1) // -2
    if len(output_str) == 0:
        output_str = "0"
    print(output_str) 

if __name__ == '__main__':
    main()
