
import sys

def main():
    input = sys.stdin.readline().strip()
    if len(input) <= 2: # if string length is <= 2, answer is 0
        print(0)
    else:
        chars = set() # use set to store unique characters
        for i in range(len(input)):
            if input[i] not in chars:
                chars.add(input[i])
            if len(chars) > 2: # if set has more than 2 chars, answer is i
                print(i)
                return
        print(len(input)) # if set has <= 2 chars, answer is length of string

if __name__ == '__main__':
    main()
