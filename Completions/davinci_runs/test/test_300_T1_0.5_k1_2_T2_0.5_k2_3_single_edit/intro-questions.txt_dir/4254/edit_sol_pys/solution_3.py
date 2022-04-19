
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read two numbers from the first line
    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")
        
# this is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
