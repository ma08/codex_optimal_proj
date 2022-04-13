

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
        attr_sort_index = attr.index(attr_sort) + 1
        songs.sort(key=lambda x: x[attr_sort_index])
        print(*attr)
        for song in songs:
            print(*song)
        print()

main()
