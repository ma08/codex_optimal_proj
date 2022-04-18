

#-----Solution-----
def main():
    #Read Input
    g1, g2, e1, e2 = map(int, input().split())
    #Calculate the number of dice sides
    g1_sides, g2_sides = g2-g1+1, e2-e1+1
    g1_prob = g1_sides/g2
    e1_prob = e1_sides/e2
    #Compare probabilities
    if g1_prob > e1_prob:
        print("Gunnar")
    elif g1_prob < e1_prob:
        print("Emma")
    else:
        print("Tie")

main()
