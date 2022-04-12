import sys

def main():
    attributes = sys.stdin.readline().rstrip().split() #read the first line, split it and store it in attributes
    songs = []
    for i in range(int(sys.stdin.readline())): #read the second line, convert it to int, and loop that many times
        songs.append(sys.stdin.readline().rstrip().split()) #read the next line, split it and store it in songs
    for i in range(int(sys.stdin.readline())): #read the third line, convert it to int, and loop that many times
        attribute = sys.stdin.readline().rstrip() #read the next line and store it in attribute
        songs.sort(key=lambda x: x[attributes.index(attribute)]) #sort songs by the attribute
        print(' '.join(attributes)) #print the attributes
        for song in songs:
            print(' '.join(song)) #print each song
        print() #print a blank line

main()
