import sys

def main():
    input_list = sys.stdin.readlines()
    input_list = [x.strip() for x in input_list]
    input_list = [x.split(' ') for x in input_list]
    input_list = [[int(y) for y in x] for x in input_list]
    n = input_list[0][0]
    input_list = input_list[1][0]
    print(n, input_list)

if __name__ == '__main__':
    main()
