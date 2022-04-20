
import sys

def main():
    n = int(sys.stdin.readline())
    names = [sys.stdin.readline() for _ in range(n)]
    count = sum(1 for i in range(n) for j in range(i+1, n) for k in range(j+1, n) if names[i][0] != names[j][0] and names[i][0] != names[k][0] and names[j][0] != names[k][0] and names[i][0] in "MARCH" and names[j][0] in "MARCH" and names[k][0] in "MARCH")
    print(count) 

if __name__ == '__main__':
    main()
