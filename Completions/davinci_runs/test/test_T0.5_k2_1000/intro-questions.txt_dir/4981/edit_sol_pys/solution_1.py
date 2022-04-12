
import sys

def main():
    input_list = [int(i) for i in sys.stdin.readline().strip().split()]
    order = [int(i) for i in sys.stdin.readline().strip().split()]
    input_list = sorted(input_list, reverse=True)
    for i in order[::-1]:
        print(input_list.pop(i), end=' ')

main()
