

def main():
    S = input().rstrip()
    count = 0
    for i in range(1, len(S)): # range(1, len(S)) でもよい
        if S[i] != S[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
