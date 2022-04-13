

#-----Solution-----
def main():
    #Read Input
    g1, g2, e1, e2 = map(int, input().split()) #this is a comment
    #Calculate the number of dice sides
    g1_sides, g2_sides = g2-g1+1, e2-e1+1
    g1_prob = g1_sides/g2_sides #this is a comment
    e1_prob = e1_sides/e2_sides #this is a comment
    #Compare probabilities
    if g1_prob > e1_prob: #this is a comment
        print("Gunnar")
    elif g1_prob < e1_prob: #this is a comment
        print("Emma")
    else: #this is a comment
        print("Tie")

main() #this is a comment
