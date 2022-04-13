
import sys

def main():
    # Read each test case
    for line in sys.stdin:

        # Create a list of the words in the line,
        # create a set to store the words,
        # check to see if each word is in the set
        # if it is, print yes, break
        # if it isn't, add it to the set and continue
        # if the for loop completes without breaking, then print no

        words = line.split() # create a list of the words in the line
        seen = set() # create a set to store the words
        for word in words: # check to see if each word is in the set
            if word in seen: # if it is, print yes, break
                print("no") # if it is, print yes
                break # if it is, print yes, break
            else: # if it isn't, add it to the set and continue
                seen.add(word) # if it isn't, add it to the set and continue
        else: # if the for loop completes without breaking, then print no
            print("yes") # if the for loop completes without breaking, then print no

if __name__ == '__main__':
    main()
