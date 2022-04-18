

#input
cards = input().split()   #splits the input by spaces and creates a list

#creates a dictionary of the ranks of the cards
rank = {'A':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0, 'J':0, 'Q':0, 'K':0}
for i in range(5):
    rank[cards[i][0]] += 1
    
#prints the maximum value of the dictionary (the number of cards of the same rank)
print(max(rank.values()))
