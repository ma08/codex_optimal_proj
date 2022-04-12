

#-----main-----#
def main():
    #read input
    attr_list = raw_input().split(" ")
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(raw_input().split(" "))
    num_commands = int(input())
    commands = []
    for i in range(num_commands):
        commands.append(raw_input())
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
