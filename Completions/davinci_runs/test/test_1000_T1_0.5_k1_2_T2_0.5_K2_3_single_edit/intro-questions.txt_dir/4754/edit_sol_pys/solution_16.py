

def main():
    n = int(input())
    socks = [int(x) for x in input().split()]

    # Check if it's impossible
    if len(socks) % 2 != 0:
        print("impossible")
        return

    # Count the number of pairs
    pairs = 0
    for sock in socks:
        pairs += socks.count(sock) // 2

    # Calculate the number of moves
    moves = n - pairs
    print(moves)

if __name__ == "__main__":
    main()
