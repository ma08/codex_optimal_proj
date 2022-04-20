
def main():
    N = int(input())
    r = int(N ** 0.5)
    for i in range(r, 0, -1):
        if N % i == 0:
            print(N // i // 10 ** (len(str(i)) - 1))
            break

if __name__ == '__main__':
    main()
