
import sys

# Read the input
def read_input():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    return n, adj


def main():
    n, adj = read_input()
    for i in range(n):
        print(len(adj[i]))



if __name__ == "__main__":
    main()
