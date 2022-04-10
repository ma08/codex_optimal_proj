

def main():
    t = int(raw_input())
    for i in range(t):
        n, m = map(int, raw_input().split())
        tiles = []
        for j in range(n):
            tiles.append(map(int, raw_input().split()))
            tiles[j].extend(map(int, raw_input().split()))
        if m % 2 == 0 and m > 2:
            print 'YES'
        else:
            print 'NO'

main()