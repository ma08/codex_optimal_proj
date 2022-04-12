import sys

def main():
    input_list = sys.stdin.readline().strip().split()
    input_list = [int(i) for i in input_list]
    order = sys.stdin.readline().strip() # read the order
    input_list = sorted(input_list)
    for i in order:
        print(input_list.pop(0), end=' ')

main()
