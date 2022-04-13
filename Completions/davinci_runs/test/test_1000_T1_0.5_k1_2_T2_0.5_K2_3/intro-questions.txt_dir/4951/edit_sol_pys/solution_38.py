
import sys, re

def main():
    #n = int(sys.stdin.readline().strip())
    #lines = []
    #for i in range(n):
    #    lines.append(sys.stdin.readline().strip().split())
    #lineCount = 1
    #for line in lines:
    #    if line[-2] != "->":
    #        print(lineCount)
    #        break
    #    else:
    #        for i in range(len(line)-2):
    #            if line[i] not in lines[:lineCount-1]:
    #                print(lineCount)
    #                break
    #    lineCount += 1
    #else:
    #    print("correct")
    line = sys.stdin.readline().strip()
    if re.match("^[a-zA-Z][a-zA-Z0-9]*$", line):
        print("OK")
    else:
        print("NG")

main()
