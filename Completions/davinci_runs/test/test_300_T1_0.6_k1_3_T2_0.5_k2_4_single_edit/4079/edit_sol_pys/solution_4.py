
def main():
    n = int(input())
    for i in range(n):
        S = input()
        S = list(S)
        S.sort()
        count = 0
        for j in range(len(S) - 1):
            if ord(S[j]) + 1 == ord(S[j + 1]):
                count += 1
        if count == len(S) - 1:
            print('Yes')
        else:
            print('No')



if __name__ == "__main__":
    main()
