import sys

def main():
    n = int(sys.stdin.readline())
    pieces = [int(x) for x in sys.stdin.readline().split()] # read line and convert to int
    pieces.sort()
    alice = 0
    bob = 0
    for i in range(n): # iterate over the pieces
        if i % 2 == 0:
            alice += pieces[n-i-1] # if i is even, alice gets the largest piece
        else:
            bob += pieces[n-i-1] # if i is odd, bob gets the largest piece
    print(alice, bob) # print the results

if __name__ == "__main__":
    main()
