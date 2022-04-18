
def main1():
    N = int(input())
    for i in range(N): 
        print(check_queens())

def check_queens():
    N = int(input())
    for i in range(N):
        x, y = [int(x) for x in input().split()] 
        for j in range(i+1, N):
            x2, y2 = [int(x) for x in input().split()] 
            if check_attack(x, y, x2, y2):
                return "INCORRECT" 
    return "CORRECT"

def check_attack(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

if __name__ == "__main__":
    main1()
