

def main():
    a,b,c = map(int,input().split())
    i,j,k = map(int,input().split())
    max_cocktails = min(a//i,b//j,c//k)
    a -= max_cocktails*i
    b -= max_cocktails*j
    c -= max_cocktails*k
    print(a,b,c)

main()
