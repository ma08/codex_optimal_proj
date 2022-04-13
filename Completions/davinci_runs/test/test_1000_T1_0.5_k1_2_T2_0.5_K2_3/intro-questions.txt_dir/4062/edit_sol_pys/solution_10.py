

def main():
    A, B = map(int, input().split())
    print(A + B if A + B < 10 else 'error')

if __name__ == '__main__':
    main()
