

import sys

def main():
    N, C = map(int, input().split())
    message = list(map(int, input().split()))

    # Create a list of lists where each element represents a character and its
    # frequency. The list is sorted in descending order of frequency.
    count = [[0] * 2 for _ in range(C + 1)]
    for i in range(N):
        count[message[i]][0] = message[i]
        count[message[i]][1] += 1
    count.sort(key=lambda x: x[1], reverse=True)

    # Append each character to the output in order of frequency.
    output = []
    for i in range(C + 1):
        if count[i][1] > 0:
            output.extend([count[i][0]] * count[i][1])

    print(" ".join(map(str, output)))

if __name__ == '__main__':
    main()
