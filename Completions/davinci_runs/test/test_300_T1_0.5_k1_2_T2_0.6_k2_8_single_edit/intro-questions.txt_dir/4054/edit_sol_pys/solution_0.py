
import sys

def main():
    # Read input
    a = list(map(int, sys.stdin.readline().split()))
    
    # Compute and print answer
    print(min(a))
    
if __name__ == '__main__':
    main()
