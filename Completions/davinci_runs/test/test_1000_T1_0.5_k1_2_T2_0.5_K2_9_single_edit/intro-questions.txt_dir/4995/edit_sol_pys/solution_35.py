
import sys

def main():
    N = int(sys.stdin.readline())
    wait_time, M, S = [], [], []
    for i in range(N):
        M.append(int(sys.stdin.readline().split()[0]))
        S.append(int(sys.stdin.readline().split()[1]))
        wait_time.append(S[i]/M[i])
    print(sum(wait_time)/len(wait_time))

if __name__ == "__main__":
    main()
