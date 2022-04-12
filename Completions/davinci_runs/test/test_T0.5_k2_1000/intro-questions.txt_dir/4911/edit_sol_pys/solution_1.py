

def main():
    """main"""
    attr = input().split()
    m = int(input())
    songs = []
    for _ in range(m):
        songs.append(input().split())
    n = int(input())
    for _ in range(n):
        attr_sort = input().split()
        sort_index = attr.index(attr_sort[0])
        songs.sort(key=lambda x: x[sort_index], reverse=True)
        print(*attr)
        for song in songs:
            print(*song)
        print()

main()
