

def main():
    K = int(input())
    A, B = map(int, input().split())

    for i in range(A, B+1):
        if i % K == 0:
            print("OK")
            return

    print("NG")

if __name__ == '__main__':
    main()