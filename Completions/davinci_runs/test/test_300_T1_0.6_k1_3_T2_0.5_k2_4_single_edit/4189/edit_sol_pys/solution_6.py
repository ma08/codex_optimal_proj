

def cheese_board():
    num_cheeses = int(input("Please enter the number of cheeses: "))
    cheeses = []
    while num_cheeses > 0:
        line = input("Please enter the cheese name followed by the price: ").split()
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
    print("There are", count, "different types of cheese.")


cheese_board()
