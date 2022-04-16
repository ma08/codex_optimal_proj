

import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    lineCount = 1
    for line in lines:
        if line[-2] != "->":
            print(lineCount)
            break
        else:
            for i in range(len(line)-2):
                for j in range(lineCount-1):
                    if line[i] in lines[j]:
                        break
                else:
                    print(lineCount) # line is not unique
                    break # break out of this line
        lineCount += 1
    else:
        print("correct")

main()
