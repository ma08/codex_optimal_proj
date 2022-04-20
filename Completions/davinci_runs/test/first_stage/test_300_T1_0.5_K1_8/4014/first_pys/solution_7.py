

import sys

def main():
    # Read the input data.
    n, m = [int(x) for x in sys.stdin.readline().split()]
    s = []
    d = []
    c = []
    for i in range(m):
        si, di, ci = [int(x) for x in sys.stdin.readline().split()]
        s.append(si)
        d.append(di)
        c.append(ci)

    # Compute the answer.
    answer = [-1] * n
    for i in range(m):
        # Check if there are enough days to prepare.
        if d[i] - s[i] < c[i]:
            print(-1)
            return

        # Check if there is a day to pass the exam.
        if d[i] - s[i] == c[i]:
            print(-1)
            return

        # Prepare for the exam.
        for j in range(c[i]):
            answer[s[i] + j - 1] = i + 1

        # Pass the exam.
        answer[d[i] - 1] = m + 1

    # Print the answer.
    for i in range(n):
        print(answer[i], end=' ')
    print()

if __name__ == '__main__':
    main()