def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(min_moves(a))

def min_moves(a):
    if len(a) % 2 != 0:
        return -1
    moves = 0
    for i in range(len(a)):
        if i % 2 != a[i] % 2:
            moves += 1
    return int(moves / 2)

if __name__ == '__main__':
    main()
