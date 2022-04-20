

def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N-1):
        if S[i] == "0" and S[i+1] == "1":
            cnt += 1
    print(cnt*2)

if __name__ == '__main__':
    main()