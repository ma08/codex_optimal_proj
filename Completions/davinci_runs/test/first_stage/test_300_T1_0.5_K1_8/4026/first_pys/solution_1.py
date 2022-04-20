

def check_if_possible(tile_types, matrix_size):
    for tile in tile_types:
        if tile[0][0] != tile[1][1] or tile[0][1] != tile[1][0]:
            return False

    if matrix_size % 2 == 0:
        return True
    else:
        return False


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        tile_types = []
        for __ in range(n):
            tile_types.append([list(map(int, input().split())), list(map(int, input().split()))])
        if check_if_possible(tile_types, m):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()