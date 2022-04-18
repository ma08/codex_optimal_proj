

import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    lineCount = 1
    for line in lines:
        if line[-2] != "->" or len(line)<3:
            print(lineCount)
            break
        else:
            for i in range(len(line)-2):
                if line[i] not in [item for sublist in lines[:lineCount-1] for item in sublist]:
                    print(lineCount)
                    break
        lineCount += 1
    else:
        print("correct")

main()
