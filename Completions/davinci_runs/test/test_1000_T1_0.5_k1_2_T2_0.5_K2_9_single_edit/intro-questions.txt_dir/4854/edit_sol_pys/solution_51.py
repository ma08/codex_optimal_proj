

import sys

def main():
    N, C = map(int, sys.stdin.readline().rstrip().split()) # N is length of the message and C is the number of distinct characters
    message = list(map(int, sys.stdin.readline().rstrip().split())) # message is the input string

    # Create a list of lists where each element represents a number and its frequency. The list is sorted in descending order of frequency.
    count = [[0] * 2 for _ in range(C + 1)]
    for i in range(N):
        count[message[i]][0] = message[i]
        count[message[i]][1] += 1
    count.sort(key=lambda x: x[1], reverse=True)

    # Append each number to the output in order of frequency
    output = []
    for i in range(C + 1):
        if count[i][1] > 0:
            output.extend([count[i][0]] * count[i][1])

        print(" ".join(map(str, output)))

if __name__ == '__main__':
    main()
