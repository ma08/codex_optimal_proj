

def main():
    s = list(input())
    t = list(input())
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
