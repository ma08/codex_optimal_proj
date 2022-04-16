
import sys

def main():
    # Read input
    a = [int(x) for x in sys.stdin.readline().split()] # a is an array
    
    # Compute and print answer
    print(min(a)) # prints the minimum value of a
    
if __name__ == '__main__':
    main()
