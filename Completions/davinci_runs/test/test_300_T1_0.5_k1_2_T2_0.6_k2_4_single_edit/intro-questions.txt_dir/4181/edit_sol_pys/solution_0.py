


def main(N, A, B):

    # For each hero, we want to find the maximum number of monsters he/she can defeat.
    # We can do this by taking the minimum of the number of monsters attacking the town
    # they are in charge of and the number of monsters attacking the town to the right.
    # We then add the number of monsters the hero can defeat to our answer.
    answer = 0
    for i in range(N):
        answer += min(A[i], B[i])
        answer += min(A[i+1], B[i])

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split(' ')]
    B = [int(x) for x in sys.stdin.readline().split(' ')]
    print(main(N, A, B))
