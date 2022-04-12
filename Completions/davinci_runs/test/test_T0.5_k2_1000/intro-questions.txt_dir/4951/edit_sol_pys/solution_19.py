
import sys

def main():
    for line in sys.stdin:
        n = int(line.strip())
        lines = []
        for i in range(n):
            lines.append(sys.stdin.readline().strip().split())
        for i in range(n):
            for j in range(i):
                if lines[j][-1] in lines[i][:-2]:
                    continue
                else:
                    print(i+1)
                    return
        print("correct")

if __name__ == "__main__":
    main()
