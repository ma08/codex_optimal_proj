import sys

def main():
    words = set() # create a set
    for line in sys.stdin:
        for word in line.split(): # split line by whitespace
            if word.lower() in words:
                print('.', end=' ') # print . if word is in set
            else:
                print(word, end=' ') # print word if word is not in set
                words.add(word.lower()) # add word to set
        print()

main()
