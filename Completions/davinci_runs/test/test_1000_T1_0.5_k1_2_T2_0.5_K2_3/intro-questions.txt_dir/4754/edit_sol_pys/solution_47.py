

def main():
    n = int(input()) # number of socks
    socks = [int(x) for x in input().split()]

    # Check if it's impossible
    if len(socks) % 2 != 0:
        print("impossible")
        return

    # Create a dictionary for the socks.
    sock_dict = {}
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1

    # Count the number of pairs.
    pairs = 0
    for sock in sock_dict:
        pairs += sock_dict[sock] // 2 # // = floor division

    # Calculate the number of moves.
    moves = n - pairs
    print(moves)

if __name__ == "__main__":
    main()
