

def cheese_board():
    num_cheeses = int(input("Enter the number of cheeses: "))
    cheeses = []
    while num_cheeses > 0:
        line = input("Enter the cheese: ").split()
        cheeses.append(line[1])
        num_cheeses -= 1

    cheeses.sort()
    cheeses.append(" ")
    i = 0
    count = 0
    while i < len(cheeses) - 1:
        if cheeses[i] != cheeses[i+1]:
            count += 1
        i += 1
    print("Number of different cheeses: ", count)


cheese_board()
