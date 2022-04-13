

def test_candy_game():
    assert candy_game([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == (6, 23, 21)
    assert candy_game([1000]) == (1, 1000, 0)
    assert candy_game([1, 1, 1]) == (2, 1, 2)
    assert candy_game([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (6, 45, 46)
    assert candy_game([2, 1]) == (2, 2, 1)
    assert candy_game([1, 1, 1, 1, 1, 1]) == (3, 4, 2)
    assert candy_game([1, 1, 1, 1, 1, 1, 1]) == (4, 4, 3)

def candy_game(candy_sizes):
    alice_score = 0
    bob_score = 0
    alice_turn = True
    moves = 0
    while len(candy_sizes) > 0:
        if alice_turn:
            alice_score += candy_sizes[0]
            candy_sizes.pop(0)
        else:
            bob_score += candy_sizes[-1]
            candy_sizes.pop()
        if alice_score > bob_score:
            alice_turn = not alice_turn
            moves += 1
        elif bob_score > alice_score:
            alice_turn = not alice_turn
            moves += 1
    return (moves, alice_score, bob_score)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        candy_sizes = list(map(int, input().split()))
        moves, alice, bob = candy_game(candy_sizes)
        print(moves, alice, bob)

if __name__ == "__main__":
    main()
