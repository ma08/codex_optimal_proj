

def main():
    A,B,C = map(int,input().split()) #(A,B,C) = (I,J,K)
    I,J,K = map(int,input().split()) #(I,J,K) = (A,B,C)
    max_cocktail = min(A//I,B//J,C//K) #max_cocktail = min(A//(I,J,K),B//(I,J,K),C//(I,J,K))
    A -= max_cocktail*I #A -= max_cocktail*(I,J,K)
    B -= max_cocktail*J #B -= max_cocktail*(I,J,K)
    C -= max_cocktail*K #C -= max_cocktail*(I,J,K)
    print(A,B,C) #print(A,B,C)

main()
