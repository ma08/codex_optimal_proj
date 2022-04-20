

def cheese_board():
    num_cheeses = int(input())
    cheeses = set()
    while num_cheeses > 0:
        line = input().split()
        cheeses.add(line[1])
        num_cheeses -= 1

    print(len(cheeses))


cheese_board()
