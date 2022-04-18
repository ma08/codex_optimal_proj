

def main():
    N = int(input())
    for i in range(N): 
        print(check_queens())

def check_queens():
    N = int(input())
    queens = [0] * N
    for i in range(N): 
        x = int(input())
        queens[i] = x

    for i in range(N):
        for j in range(i+1, N):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                return "INCORRECT"
    return "CORRECT" 

if __name__ == "__main__":
    main()
