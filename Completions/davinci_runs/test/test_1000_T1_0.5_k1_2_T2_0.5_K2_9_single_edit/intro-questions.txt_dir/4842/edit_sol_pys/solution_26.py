import sys
import math

def main():
    """
    Main function
    """
    input_list = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print(math.floor(input_list[0]/input_list[1]))

if __name__ == '__main__':
    main()
