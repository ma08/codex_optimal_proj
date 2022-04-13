import sys

def main():
    N = int(sys.stdin.readline())
    wait_time = 0
    for i in range(N):
        M, S = map(int, sys.stdin.readline().split())
        wait_time += S/M
    print(wait_time/N)

if __name__ == "__main__":
    main()
