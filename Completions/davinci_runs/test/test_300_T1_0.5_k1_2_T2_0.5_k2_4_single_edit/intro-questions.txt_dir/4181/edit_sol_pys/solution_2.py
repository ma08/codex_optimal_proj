
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split(' ')]
    b = [int(x) for x in sys.stdin.readline().split(' ')]

    # For each hero, we want to find the maximum number of monsters he/she can defeat.
    # We can do this by taking the minimum of the number of monsters attacking the town
    # they are in charge of and the number of monsters attacking the town to the right.
    # We then add the number of monsters the hero can defeat to our answer.
    answer = 0
    for i in range(n):
        answer += min(a[i], b[i])
        answer += min(a[i+1], b[i])

    print(answer)

if __name__ == '__main__':
    main()
