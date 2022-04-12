

def main():
    n = int(input())  # Number of socks
    socks = [int(x) for x in input().split()]  # List of socks

    # Check if it's impossible to find a solution (odd number of socks)
    if len(socks) % 2 != 0:
        print("impossible")
        return

    # Create a dictionary for the socks (key: sock color, value: number of socks)
    sock_dict = {}
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1

    # Count the number of pairs (if the number of socks is even, there is a pair)
    pairs = 0
    for sock in sock_dict:
        pairs += sock_dict[sock] // 2  # Integer division

    # Calculate the number of moves (number of socks - number of pairs)
    moves = n - pairs
    print(moves)

if __name__ == "__main__":
    main()
