#!/usr/bin/env python3

def main():
    n = int(input())
    e = int(input())
    songs = set()
    for _ in range(e):
        for i in input().split()[1:]:
            songs.add(i)
    for i in range(1,n+1):
        if str(i) not in songs:
            print(i)
#
if __name__ == "__main__":
    main()
