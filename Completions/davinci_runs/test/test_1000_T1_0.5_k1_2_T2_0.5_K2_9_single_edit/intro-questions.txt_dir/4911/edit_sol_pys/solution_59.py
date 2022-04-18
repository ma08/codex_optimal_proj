

def main():
    """main"""
    attr = input().split()
    m = int(input())
    songs = []
    for _ in range(m):
        songs.append(input().split())
    n = int(input())
    for _ in range(n):
        attr_sort = input()
        songs.sort(key=lambda x: x[attr.index(attr_sort)])
        print(*attr)
        for song in songs:
            print(*song)
        print()

main()
