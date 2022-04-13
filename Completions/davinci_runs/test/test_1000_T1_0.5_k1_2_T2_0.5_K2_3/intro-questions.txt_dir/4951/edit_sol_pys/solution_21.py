
import sys

def main():
    n = int(sys.stdin.readline().strip())
    words = []
    for i in range(n):
        words.append(sys.stdin.readline().strip().split())
    for i in range(n):
        for j in range(i):
            if words[j][-1] in words[i][:-2]:
                continue
            else:
                print(i + 1)
                return
    print("correct")

if __name__ == "__main__":
    main()
