import sys

def main():
    N = int(input())
    sys.stdin.readline()
    queens = []
    for i in range(N):
        x, y = [int(x) for x in sys.stdin.readline().split()]
        queens.append((x,y))
    print(check_queens(queens))

def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if check_attack(queens[i], queens[j]):
                return "INCORRECT"
    return "CORRECT"

def check_attack(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

if __name__ == "__main__":
    main()
