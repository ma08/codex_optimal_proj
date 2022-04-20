

def main():
    A, B = map(int, input().split())
    if A%3 == 0 or B%3 == 0 or (A+B)%3 == 0:
        print(-1)
    else:
        print(A*B)

if __name__ == '__main__':
    main()