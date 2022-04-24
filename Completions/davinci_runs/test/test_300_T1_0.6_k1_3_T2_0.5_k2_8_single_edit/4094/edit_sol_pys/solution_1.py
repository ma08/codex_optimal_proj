

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print('\t', end='')
    for i in range(c, d+1):
        print(i, end='\t')
    print()
    for j in range(a, b+1):
        print(j, end='\t')
        for k in range(c, d+1):
            print(j*k, end='\t')
        print()

if __name__ == '__main__':
    main()
