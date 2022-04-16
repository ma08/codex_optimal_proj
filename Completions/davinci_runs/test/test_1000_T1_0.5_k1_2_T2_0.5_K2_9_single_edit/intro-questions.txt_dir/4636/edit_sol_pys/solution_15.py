
def test_candy_game(candy_sizes):
    assert candy_game(candy_sizes) == (6, 23, 21)

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

if __name__ == "__main__":
    main()
