
import sys

def main():
    input_num = sys.stdin.readline()
    output_str = ""    
    for i in range(len(input_num)):
        if input_num[i] == '1':
            output_str += '0'
        else:
            output_str += '1'
    print(int(output_str, 2))

if __name__ == '__main__':
    main()
