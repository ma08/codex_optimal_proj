

def test_candy_game_function():
    assert candy_game_function([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == (3, 23, 21)
    assert candy_game_function([1000]) == (1, 1000, 0, 1)
    assert candy_game_function([1, 1, 1]) == (2, 1, 2, 2)
    assert candy_game_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (6, 45, 46, 6)
    assert candy_game_function([2, 1]) == (1, 2, 1, 1)
    assert candy_game_function([1, 1, 1, 1, 1, 1]) == (2, 4, 2, 3)
    assert candy_game_function([1, 1, 1, 1, 1, 1, 1]) == (2, 4, 3, 4)

def candy_game_function(candy_sizes):
    alice_score = 0
    bob_score = 0
    alice_turn = False
    moves = 0
    while len(candy_sizes) > 0:
        if alice_turn:
            alice_score += candy_sizes[0]
            candy_sizes.pop(0)
            alice_turn = not alice_turn
        else:
            bob_score += candy_sizes[-1]
            candy_sizes.pop()
            alice_turn = not alice_turn
        moves += 1
    return (moves, alice_score, bob_score, moves)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        candy_sizes = list(map(int, input().split()))
        moves, alice, bob, total_moves = candy_game_function(candy_sizes)
        print(total_moves, alice, bob)

if __name__ == "__main__":
    main()
