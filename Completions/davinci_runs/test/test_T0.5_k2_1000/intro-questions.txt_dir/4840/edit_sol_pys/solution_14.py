

#-----Solution-----
def main():
    #Read Input
    g1, g2, e1, e2 = map(int, input().split())
    #Calculate the number of dice sides
    g_sides, e_sides = g2-g1+1, e2-e1+1
    g_prob = g_sides/g2
    e_prob = e_sides/e2
    #Compare probabilities
    if g_prob > e_prob:
        print("Gunnar")
    elif g_prob < e_prob:
        print("Emma")
    else:
        print("Tie")

main()
