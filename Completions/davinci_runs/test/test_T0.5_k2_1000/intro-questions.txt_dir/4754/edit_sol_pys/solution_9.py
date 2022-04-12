
import math
import sys

def main():
    n = int(input().strip())
    socks = list(map(int, input().strip().split()))

    # if len(socks) % 2 != 0:
    #     print("impossible")
    #     return

    count = 0 
    # Sort socks by type.
    socks = sorted(socks) 
    # Count number of socks of each type.
    socks_count = {} 
    for sock in socks:
        if sock in socks_count: 
            socks_count[sock] += 1 
        else: 
            socks_count[sock] = 1 
    # Count number of moves.
    for sock, num_socks in socks_count.items(): 
        if num_socks % 2 == 0: 
            count += num_socks 
        else: 
            count += num_socks - 1 
            if len(socks_count) == 1: 
                print("impossible") 
                return 
    print(count) 

if __name__ == "__main__": 
    main() 
