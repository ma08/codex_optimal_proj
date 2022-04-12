

def main():
    n = int(input())
    socks = [int(x) for x in input().split()]

    # Check if it's impossible
    if n % 2 != 0:
        print("impossible")
        return

    # Create a dictionary for the socks and count the number of pairs
    sock_dict = {}
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1
    pairs = 0
    for sock in sock_dict:
        pairs += sock_dict[sock] // 2

    # Calculate the number of moves and print it
    moves = n - pairs
    print(moves)

if __name__ == "__main__":
    main()
