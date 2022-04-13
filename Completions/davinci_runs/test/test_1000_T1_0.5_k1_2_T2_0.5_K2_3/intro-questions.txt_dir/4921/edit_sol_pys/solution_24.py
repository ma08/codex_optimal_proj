
import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.lower().split() #convert to lower case and split
        for word in line:
            if word in words: #if word is in the list
                print(".", end=" ") #print "."
            else:
                words.append(word) #add word to list
                print(word, end=" ") #print word
        print() #new line

main()
