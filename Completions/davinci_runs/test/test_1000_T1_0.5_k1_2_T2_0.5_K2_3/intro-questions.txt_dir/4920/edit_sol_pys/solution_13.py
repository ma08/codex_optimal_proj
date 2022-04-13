

import sys

def main():
    s = sys.stdin.readline().strip()  # read a line from stdin and remove the trailing new line character
    count = 0
    for i in range(len(s)):  # iterate over all characters in the string
        for j in range(i + 1, len(s)):  # iterate over all characters following the first character
            if s[i] != s[j]:  # check if the characters are different
                if s[i] not in s[i+1:j] and s[j] not in s[i+1:j]:  # check if both characters do not appear between the two characters
                    count += 1
    print(count)

if __name__ == "__main__":

    main()
