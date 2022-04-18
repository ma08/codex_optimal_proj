
import sys

def main():
    """
    Main function
    """
    input_list = [int(x) for x in sys.stdin.readline().split(' ')]
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
    print(degree, input_list[0]*degree)

if __name__ == '__main__':
    main()
