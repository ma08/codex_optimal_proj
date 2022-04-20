
def main():
    N = int(input())
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            print(len(str(i)))
            break

if __name__ == '__main__':
    main()