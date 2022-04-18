

def main():
    S = input()
    print ("AC") if S[0] == "A" and S[2:-1].count("C") == 1 and S.count(S[0]) == 1 and S.count(S[2]) == 1 and S[1:-1].islower() else print("WA")

main()
