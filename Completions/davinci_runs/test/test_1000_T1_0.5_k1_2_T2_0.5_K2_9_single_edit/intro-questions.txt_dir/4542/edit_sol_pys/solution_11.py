

def main():
    S = input()
    count = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
    if S[-1] == '+':
        count += 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()
