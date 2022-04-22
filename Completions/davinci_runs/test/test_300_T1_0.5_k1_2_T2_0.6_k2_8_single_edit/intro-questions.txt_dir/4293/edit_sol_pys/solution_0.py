

P, Q, R = map(int, input().split())



def main():
    S = input()
    T = input()
    if S == T:
        print("same")
    elif S.lower() == T.lower():
        print("case-insensitive")
    else:
        print("different")
    return


if __name__ == "__main__":
    main()
print(min(P+Q, Q+R, R+P))
