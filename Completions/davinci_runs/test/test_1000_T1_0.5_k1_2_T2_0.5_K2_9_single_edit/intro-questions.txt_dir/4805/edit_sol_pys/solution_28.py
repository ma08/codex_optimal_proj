

import sys

def main():
    # Read each test case
    for line in sys.stdin:
        # Create a list of the words in the line
        words = line.split()
        # Check to see if the words are the same
        if words[0] == words[1]:
            print("yes")
        else:
            # If the for loop completes without breaking, then print yes
            print("yes")

if __name__ == '__main__':
    main()
