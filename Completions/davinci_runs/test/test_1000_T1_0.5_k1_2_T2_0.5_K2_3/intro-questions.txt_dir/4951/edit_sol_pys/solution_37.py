import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    lineCount = 1
    lineCount2 = 0
    for line in lines[:]:
        if line[-2] != "->":
            print(lineCount2+1)
            exit()
        else:
            for i in range(len(line)-2):
                if line[i] not in lines[:lineCount]:
                    print(lineCount2+1)
                    exit()
        lineCount += 1
        lineCount2 += 1
    else:
        print("correct")

main()
