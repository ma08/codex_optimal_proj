

import sys

def main():
    n = int(input().strip())
    lines = []
    for i in range(n):
        lines.append(input().strip().split())
    lineCount = 1
    for line in lines:
        if line[-2] != "->":
            print(lineCount)
            break
        else:
            for i in range(len(line)-2):
                if line[i] not in lines[:lineCount-1]:
                    print(lineCount)
                    break
        lineCount += 1
    else:
        print("correct")

main()
