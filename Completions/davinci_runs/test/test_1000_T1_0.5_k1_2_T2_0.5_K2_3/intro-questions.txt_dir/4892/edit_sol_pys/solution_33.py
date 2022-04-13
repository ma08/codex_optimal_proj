import sys

def main():
    n = int(sys.stdin.readline())

    probabilities = []

    for _ in range(n):
        prob = sys.stdin.readline().split()
        probabilities.append(float(prob[1]))

    probabilities.sort()
    probabilities.reverse()

    total = 0
    for i in range(n):
        total += (i + 1) * probabilities[i]

    print("{:.4f}".format(total))

if __name__ == '__main__':
    main()
