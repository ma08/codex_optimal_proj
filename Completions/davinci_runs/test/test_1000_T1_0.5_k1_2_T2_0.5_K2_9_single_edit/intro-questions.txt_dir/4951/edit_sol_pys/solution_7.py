
import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    for i in range(n-1):
        if lines[i][-1] not in lines[i+1][:-2]:
            print(i+2)
            return
    print("correct")

if __name__ == "__main__":
    main()
