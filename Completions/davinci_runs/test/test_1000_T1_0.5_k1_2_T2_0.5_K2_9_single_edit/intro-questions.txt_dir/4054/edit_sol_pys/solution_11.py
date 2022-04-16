
import sys

def main():
    # Read input
    a = [int(x) for x in sys.stdin.readline().split()]  # read input
    print(min(a))  # print answer
    
if __name__ == '__main__':
    main()
