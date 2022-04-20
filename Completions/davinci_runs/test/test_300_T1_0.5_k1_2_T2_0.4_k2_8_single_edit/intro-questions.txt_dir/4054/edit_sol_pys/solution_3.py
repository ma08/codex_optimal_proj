
import sys

def main():
    # Read input
    a = [int(x) for x in sys.stdin.readline().split()] # split into list
    
    # Compute and print answer
    print(min(a)) # find minimum value
    
if __name__ == '__main__':
    main()
