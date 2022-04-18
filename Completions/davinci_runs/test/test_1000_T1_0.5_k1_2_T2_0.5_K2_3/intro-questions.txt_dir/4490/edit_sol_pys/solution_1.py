
def main():
    b = input().strip()
    if b == 'A':
        print('T', end='')
    elif b == 'T':
        print('A', end='')
    elif b == 'C':
        print('G', end='')
    elif b == 'G':
        print('C', end='')

if __name__ == '__main__':
    main()
