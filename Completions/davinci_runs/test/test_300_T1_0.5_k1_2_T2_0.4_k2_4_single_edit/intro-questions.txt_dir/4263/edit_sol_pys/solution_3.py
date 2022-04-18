
import sys

def main():
    S = sys.stdin.readline().rstrip() # rstrip() removes the newline character
    max_len = 0 # the longest length of a substring
    curr_len = 0 # the current length of a substring
    for c in S: # for each character in the string
        if c == 'A' or c == 'C' or c == 'G' or c == 'T': # if the character is a nucleotide
            curr_len += 1 # increment the current length
        else: # if the character is not a nucleotide
            if curr_len > max_len: # if the current length is greater than the longest length
                max_len = curr_len # set the longest length equal to the current length
            curr_len = 0 # reset the current length to 0
    if curr_len > max_len: # if the current length is greater than the longest length
        max_len = curr_len # set the longest length equal to the current length
    print(max_len) # print the longest length

if __name__ == '__main__':
    main()
