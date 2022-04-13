import sys

def main():
    # Read the input
    n, k = map(int, sys.stdin.readline().split())

    # Compute the expected score
    expectedScore = 0
    for i in range(1, n+1):
        # Compute the probability of rolling i
        probability = 1/float(n)

        # Compute the expected score of rolling i
        score = i

        # If we can roll again, compute the expected score for that roll
        if k > 1:
            for j in range(1, n+1):
                # Compute the probability of rolling j
                probability *= 1/float(n)

                # Compute the expected score of rolling j
                score += j

        # Add the expected score of this roll to the total expected score
        expectedScore += probability*score

    # Print the expected score
    print(expectedScore)

if __name__ == '__main__':
    main()
