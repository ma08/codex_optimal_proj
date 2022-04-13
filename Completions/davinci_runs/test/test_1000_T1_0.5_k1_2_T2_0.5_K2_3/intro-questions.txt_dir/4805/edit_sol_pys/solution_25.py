

import sys

def main():
    words = sys.stdin.readline().strip().split() #get input from user, split into list
    phrase = set()
    for word in words: #for each word in the list
        if word in phrase:
            print('no') #if word is already in the list, print no
            return #stop the function
        phrase.add(word) #if word is not in the list, add it to the list
    print('yes') #if the function makes it this far without printing no, print yes

if __name__ == '__main__':
    main()
