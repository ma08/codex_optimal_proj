
import sys

def main():
    N, T, M = map(int, sys.stdin.readline().split())  # N:number of people, T:time, M:number of buses
    print(N*T*M)  # total time

if __name__ == "__main__":
    main()
