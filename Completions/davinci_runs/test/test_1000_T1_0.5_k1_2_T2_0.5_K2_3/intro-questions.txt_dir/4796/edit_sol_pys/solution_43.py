

def main():
    A,B,C = map(int,input().split()) #A,B,C are the number of oranges, lemons, and limes available
    I,J,K = map(int,input().split()) #I,J,K are the number of oranges, lemons, and limes in a single cocktail
    max_cocktail = min(A//I,B//J,C//K)
    A -= max_cocktail*I
    B -= max_cocktail*J
    C -= max_cocktail*K
    print(max_cocktail,A,B,C)

main()
