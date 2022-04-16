

def main():
    A,B,C = map(int,input().split())
    X,Y,Z = map(int,input().split())
    max_cocktail = min(A//X,B//Y,C//Z)
    A -= max_cocktail*X
    B -= max_cocktail*Y
    C -= max_cocktail*Z
    print(A,B,C,max_cocktail)

main()
