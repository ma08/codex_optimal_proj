

def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("No")
        return

    if S[:N // 2] == S[N // 2:]:
        print("Yes")
    else: 
        print("No")



if __name__ == '__main__':
    main()
