

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(len(set(a)))
    print(' '.join([str(i) for i in set(a)]))

if __name__ == '__main__':
    main()
