

def min_changes(S, T):
    count = 0  # initialize count
    for i in range(len(T)):
        if S[i] != T[i]:
            count += 1  # increment count
    return count  # return count

def main():
    S = input()
    T = input()
    print(min_changes(S, T))

if __name__ == '__main__':
    main()
