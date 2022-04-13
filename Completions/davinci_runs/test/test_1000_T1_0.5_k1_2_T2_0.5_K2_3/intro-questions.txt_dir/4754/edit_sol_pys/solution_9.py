

def main():
    n = int(input())
    socks = [int(i) for i in input().split()]
    socks.sort()

    # If there are socks of the same type, try paring them first.
    for i in range(0, len(socks), 2):
        if socks[i] == socks[i+1]:
            socks.pop(i)
            socks.pop(i)
            n -= 1
    
    # If there are no socks left, we are done.
    if not socks:
        return 0
    
    # If there are an odd number of socks left, there is no solution.
    if len(socks) % 2 == 1:
        return "Impossible"

    # Try to pair the remaining socks.
    moves = 0
    while socks:
        # If the top sock is a match for the bottom sock, pair them up.
        if socks[0] == socks[-1]:
            socks.pop(0)
            socks.pop(-1)
            moves += 2
            continue

        # If the top sock is not a match for the bottom sock, try paring it with the second from the bottom sock.
        if socks[0] == socks[-2]:
            socks.pop(0)
            socks.pop(-2)
            moves += 2
            continue

        # If the top sock is not a match for any other sock, there is no solution.
        return "Impossible"

    return moves

if __name__ == "__main__":
    print(main())
