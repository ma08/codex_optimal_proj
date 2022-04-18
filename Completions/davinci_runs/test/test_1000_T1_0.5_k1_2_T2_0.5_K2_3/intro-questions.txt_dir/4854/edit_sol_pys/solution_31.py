
import sys

def main():
    N, C = map(int, sys.stdin.readline().rstrip().split())
    message = list(map(int, sys.stdin.readline().rstrip().split()))

    # Create a list of lists where each element represents a number and its frequency.
    # The list is sorted in descending order of frequency.
    count = [[0, 0] for _ in range(C + 1)]
    for i in range(N):
        count[message[i]][0] += 1
        count[message[i]][1] += 1
    count.sort(key=lambda x: x[0], reverse=True)

    # Append each number to the output in order of frequency.
    output = []
    for i in range(C + 1):
        if count[i][0] > 0:
            output.extend([count[i][1]] * count[i][0])

    print(" ".join(map(str, output)))

if __name__ == '__main__':
    main()
