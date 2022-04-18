

def main():
    S = input()
    T = input()
    if sorted(S) < sorted(T, reverse=True):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
