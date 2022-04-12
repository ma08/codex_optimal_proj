

def main():
    n = int(input())  # Number of socks
    socks = [int(x) for x in input().split()]

    # Create a dictionary for the socks and count the number of pairs
    sock_dict = {}  # Dictionary to store the socks
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1  # Add the sock to the dictionary

    pairs = 0  # Number of pairs
    for sock in sock_dict:
        pairs += sock_dict[sock] // 2  # Add the number of pairs of the sock to the total number of pairs

    # Calculate the number of moves and print it
    moves = n - pairs  # Number of moves
    print(moves)

if __name__ == "__main__":
    main()
