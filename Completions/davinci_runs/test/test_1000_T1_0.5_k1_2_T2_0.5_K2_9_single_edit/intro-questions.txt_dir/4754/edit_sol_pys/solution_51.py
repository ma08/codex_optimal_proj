

def main():
    n = int(input())
    socks = [int(x) for x in input().split()]

    # Check if it's impossible
    if len(socks) % 2 != 0:
        print("impossible")
        return

    # Create a dictionary for the socks
    socks_dict = {}
    for sock in socks:
        socks_dict[sock] = socks_dict.get(sock, 0) + 1

    # Count the number of pairs
    pairs = 0
    for sock in socks_dict:
        pairs += socks_dict[sock] // 2

    # Calculate the number of moves
    moves = n - pairs
    print(moves)

if __name__ == "__main__":
    main()
