# this is a comment
import sys

def main():
    # Read each test case
    for line in sys.stdin:
        # Create a list of the words in the line
        words = line.split()
        # Create a set to store the words
        seen = set()
        # Check to see if each word is in the set
        for word in words:
            if word in seen:
                # If it is, print no
                print("no")
                break
            else:
                # If it isn't, add it to the set and continue
                seen.add(word)
        else:
            # If the for loop completes without breaking, then print yes
            print("yes")


if __name__ == '__main__':
    main()
