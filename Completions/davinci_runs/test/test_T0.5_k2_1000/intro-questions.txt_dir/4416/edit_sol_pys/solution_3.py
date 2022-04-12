
import sys

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, k = next(reader)
    books = sorted(reader, key=lambda x: x[0])

    # if there are enough books that Alice likes, then the optimal solution
    # will be the k books that Alice likes with the smallest cost
    alice_likes = [t for t, a, b in books if a == 1]
    if len(alice_likes) >= k:
        print(sum(alice_likes[:k]))
        return

    # otherwise, we need to find the maximum number of books
    # that Bob likes and add them to the books that Alice likes
    bob_likes = [t for t, a, b in books if b == 1]
    num_extra_bob = k - len(alice_likes)
    print(sum(alice_likes) + sum(bob_likes[:num_extra_bob]))

main()
