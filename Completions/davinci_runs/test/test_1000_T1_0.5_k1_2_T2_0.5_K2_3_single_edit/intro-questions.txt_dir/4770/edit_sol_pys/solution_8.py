

import sys

def main():
    N, M = [int(x) for x in input().split()]

    if N > M:
        print("Dr. Chaz needs {} more piece[s] of chicken!".format(N - M))
    else:
        print("Dr. Chaz will have {} piece[s] of chicken left over!".format(M - N))

if __name__ == "__main__":
    main()
