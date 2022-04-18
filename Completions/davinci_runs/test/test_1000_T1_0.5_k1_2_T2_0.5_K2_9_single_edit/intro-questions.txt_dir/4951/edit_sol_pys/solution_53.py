
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        for j in range(i):
            if line[-1] in lines[j][:-2]:
                break
        else:
            print(i+1)
            return
    else:
        print("correct")

if __name__ == "__main__":
    main()
