

def cheese_board():
    num_cheeses = int(input())
    cheeses = []
    while num_cheeses > 0:
        line = input().split()
        cheeses.append(line[1])
        num_cheeses -= 1

    cheeses.sort()
    cheeses.append(" ")
    count = 0
    for i in range(0, len(cheeses) - 1):
        if cheeses[i] != cheeses[i+1]:
            count += 1
    print(count)


cheese_board()
