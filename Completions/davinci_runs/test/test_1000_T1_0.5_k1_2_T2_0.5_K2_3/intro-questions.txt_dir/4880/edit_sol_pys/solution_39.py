
import sys

def main():
    """
    Main function.
    """
    # Read the first line
    line = sys.stdin.readline()
    # Read the second line
    line = sys.stdin.readline()
    # Read the third line
    line = sys.stdin.readline()
    # Print the result, removing the trailing newline
    print(line.rstrip())

if __name__ == '__main__':
    main()
