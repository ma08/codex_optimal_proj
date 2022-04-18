import sys


#-----main-----
def main():
    #read input
    attr_list = sys.stdin.readline().split(" ")
    num_songs = int(sys.stdin.readline())
    songs = []
    for i in range(num_songs):
        songs.append(sys.stdin.readline().split(" "))
    num_commands = int(sys.stdin.readline())
    commands = []
    for i in range(num_commands):
        commands.append(sys.stdin.readline())
    #sort
    for command in commands:
        songs = sorted(songs, key=lambda x: x[attr_list.index(command)])
        #print
        print(" ".join(attr_list))
        for song in songs:
            print(" ".join(song))
        print()

if __name__ == "__main__":
    main()
