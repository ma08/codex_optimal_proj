#!/usr/bin/env python3

#-----main-----
def main():
    #read inputs
    attr_list = input().split(" ")
    num_songs = int(input())
    songs = []
    for i in range(num_songs):
        songs.append(input().split(" "))
    num_commands = int(input())
    commands = []
    for i in range(num_commands):
        commands.append(input())
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
