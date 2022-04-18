

def main():
    n = int(input())  # Number of socks
    socks = [int(x) for x in input().split()]

    # Check if it's impossible (odd number of socks)
    if len(socks) % 2 != 0:
        print("Impossible")
        return

    # Create a dictionary for the socks, with the key being the colour
    # and the value being the number of socks of that colour
    sock_dict = {}
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1

    # Count the number of pairs
    pairs = 0
    for sock in sock_dict:
        pairs += sock_dict[sock] // 2

    # Calculate the number of moves (number of socks - number of pairs)
    print(n - pairs)

if __name__ == "__main__":
    main()
