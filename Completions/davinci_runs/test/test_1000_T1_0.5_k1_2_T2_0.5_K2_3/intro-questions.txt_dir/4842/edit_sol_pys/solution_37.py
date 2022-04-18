
import sys

def main():
    input_list = sys.stdin.readlines()
    input_list = [x.strip() for x in input_list]
    input_list = [x.split(' ') for x in input_list]
    input_list = [[int(y) for y in x] for x in input_list]
    input_list = input_list[0]
    n = input_list[0]
    input_list = input_list[1:]
    degree = 0
    while True:
        degree += 1
        if len(set(input_list)) == 1:
            break
        else:
            temp_input = []
            for i in range(len(input_list)-1):
                temp_input.append(input_list[i+1]-input_list[i])
            input_list = temp_input
    print(degree, input_list[0]*(degree+1))

if __name__ == '__main__':
    main()
