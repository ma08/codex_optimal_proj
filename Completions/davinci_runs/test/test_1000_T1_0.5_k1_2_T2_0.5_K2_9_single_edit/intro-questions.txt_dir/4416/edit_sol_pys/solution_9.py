
import sys

    sys.stdin = open('input.txt')
def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, k = next(reader)
    books = sorted(reader, key=lambda x: x[0])

    # if there are enough books that Bob likes, then the optimal solution
    # will be the k books that Bob likes with the smallest cost
    bob_likes = [t for t, a, b in books if b == 1]
    if len(bob_likes) >= k:
        print(sum(bob_likes[:k]))
        return 

    # otherwise, we need to find the minimum number of books
    # that Bob likes and add them to the books that Alice likes
    alice_likes = [t for t, a, b in books if a == 1]
    num_extra_bob = k - len(alice_likes)
    print(sum(alice_likes) + sum(bob_likes[:num_extra_bob]))

main()
