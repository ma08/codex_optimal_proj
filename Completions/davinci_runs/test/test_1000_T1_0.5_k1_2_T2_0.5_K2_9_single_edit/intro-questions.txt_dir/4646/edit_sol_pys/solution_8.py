

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(min_moves(n))

def min_moves(n):
    if n % 2 != 0:
        return -1
    moves = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            moves += 1
    return int(moves / 2)

if __name__ == '__main__':
    main()
