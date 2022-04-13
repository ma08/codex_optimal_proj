

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]  # Create a list of the socks.
    socks.sort()

    # If there are socks of the same type, try pairing them first.
    for i in range(0, len(socks), 2):  # Step through the list in pairs.
        if socks[i] == socks[i+1]:
            socks.pop(i)  # Remove the pair of socks.
            n -= 1
    
    # If there are no socks left, we are done.
    if len(socks) == 0:  # If the list is empty, return 0.
        return 0
    
    # If there is an odd number of socks left, there is no solution.
    if len(socks) % 2 == 1:  # If the list has an odd number of socks, return "impossible".
        return "impossible"

    # Try to pair up the remaining socks.
    moves = 0
    while len(socks) > 0:  # While there are still socks in the list...
        # If the top sock is a match for the bottom sock, pair them.
        if socks[0] == socks[-1]:
            socks.pop(0)  # Remove the top sock.
            socks.pop(-1)  # Remove the bottom sock.
            moves += 2
            continue

        # If the top sock is not a match for the bottom sock, try pairing it with the second from the bottom sock.
        if socks[0] == socks[-2]:
            socks.pop(0)  # Remove the top sock.
            socks.pop(-2)  # Remove the second from the bottom sock.
            moves += 2
            continue

        # If the top sock is not a match for any other sock, there is no solution.
        return "impossible"

    return moves

if __name__ == "__main__":
    print(main())
