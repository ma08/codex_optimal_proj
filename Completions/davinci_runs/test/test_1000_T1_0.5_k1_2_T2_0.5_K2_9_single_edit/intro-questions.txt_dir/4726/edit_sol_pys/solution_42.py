

def main():
    N = int(input())
    S = input()
    for i in range(N):
        print(S[i], end='')
        if (i+1) % 10 == 0:
            print()

if __name__ == "__main__":
    main()
