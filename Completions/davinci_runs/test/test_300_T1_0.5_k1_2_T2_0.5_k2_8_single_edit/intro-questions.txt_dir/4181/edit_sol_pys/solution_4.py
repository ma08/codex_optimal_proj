import sys

def main():
    N, M = [int(x) for x in sys.stdin.readline().split(' ')]
    A = [int(x) for x in sys.stdin.readline().split(' ')] # A[i] is the number of monsters attacking town i
    B = [int(x) for x in sys.stdin.readline().split(' ')] # B[i] is the number of monsters hero i can defeat
    C = [int(x) for x in sys.stdin.readline().split(' ')] # C[i] is the number of towns hero i can defend
    D = [int(x) for x in sys.stdin.readline().split(' ')] # D[i] is the town hero i is in charge of
if __name__ == '__main__':
    main()
