
def main():
    """main function"""
    attr = input().split()
    m = int(input())
    songs = []
    for _ in range(m):
        songs.append(input().split())
    n = int(input())
    for _ in range(n):
        attr_sort = input()
        attr_sort_in = attr.index(attr_sort)
        songs.sort(key=lambda x: x[attr_sort_in])
        print(*attr)
        for song in songs:
            print(*song)
        print()

main()
