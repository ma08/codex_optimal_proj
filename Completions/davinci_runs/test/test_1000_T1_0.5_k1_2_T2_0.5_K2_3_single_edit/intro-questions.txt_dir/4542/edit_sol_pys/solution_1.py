

def main():
    S = input()
    count = 0
    for i in range(1, len(S)):  # range(1, len(S)) は、インデックス1からlen(S)-1まで
        if S[i] != S[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
