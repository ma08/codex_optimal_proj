

def main():
    N = int(input())
    queens = set()
    for i in range(N):
        x, y = [int(x) for x in input().split()]
        queens.add((x,y))
    print(check_queens(queens))

def check_queens(queens):
    for q1 in queens:
        for q2 in queens:
            if check_attack(q1, q2) and q1 != q2:
                return "INCORRECT"
    return "CORRECT"

def check_attack(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

if __name__ == "__main__":
    main()
