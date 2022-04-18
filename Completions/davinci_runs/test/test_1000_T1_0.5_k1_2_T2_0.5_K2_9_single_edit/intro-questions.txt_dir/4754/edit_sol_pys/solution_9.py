

def main():
    n = int(input())
    socks = [int(x) for x in input().split()]

    # Check if it's impossible
    if n % 2 != 0:
        print("impossible")
        return 0

    # Create a dictionary for the socks
    sock_dict = {}
    for sock in socks:
        sock_dict[sock] = sock_dict.get(sock, 0) + 1

    # Count the number of pairs
    pairs = 0
    for sock in sock_dict.keys():
        pairs += sock_dict[sock] // 2 # "//" is integer division

    # Calculate the number of moves
    return n - pairs

if __name__ == "__main__":
    print(main())
