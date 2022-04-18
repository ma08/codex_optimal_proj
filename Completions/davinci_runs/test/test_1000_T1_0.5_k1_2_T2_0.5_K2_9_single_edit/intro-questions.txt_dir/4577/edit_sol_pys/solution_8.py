

def main():
    a,b,c = [int(x) for x in input().split()]
    if a <= c <= b:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
