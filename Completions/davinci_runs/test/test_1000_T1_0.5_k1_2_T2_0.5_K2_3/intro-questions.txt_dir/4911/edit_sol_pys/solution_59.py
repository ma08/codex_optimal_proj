

def main():
    """main"""
    attr = input().split(',')
    m = int(input())
    songs = []
    for _ in range(m):
        songs.append(input().split(','))
    n = int(input())
    for _ in range(n):
        attr_sort = input()
        attr_sort_idx = attr.index(attr_sort)
        songs.sort(key=lambda x: x[attr_sort_idx])
        print(*attr)
        for song in songs:
            print(*song)
        print()

main()
