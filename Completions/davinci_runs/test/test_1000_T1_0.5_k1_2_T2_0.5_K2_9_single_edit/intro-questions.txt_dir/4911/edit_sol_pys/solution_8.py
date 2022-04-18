

#-----main-----
def main():
    #read input
    attr_list = input().split()
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input().split())
    num_commands = int(input())
    commands = []
    for i in range(num_commands):
        commands.append(input())
    #sort
    for command in commands:
        songs = sorted(songs, key=lambda x: x[attr_list.index(command)])
        #print
        print(*attr_list)
        for song in songs:
            print(*song)
        print()

if __name__ == "__main__":
    main()
