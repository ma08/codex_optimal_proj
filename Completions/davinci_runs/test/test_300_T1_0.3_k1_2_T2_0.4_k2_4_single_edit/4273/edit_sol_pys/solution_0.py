
#
import sys

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if names[i][0] == names[j][0] or names[i][0] == names[k][0] or names[j][0] == names[k][0]:
                    continue
                if names[i][0] != "M" and names[i][0] != "A" and names[i][0] != "R" and names[i][0] != "C" and names[i][0] != "H":
                    continue
                if names[j][0] != "M" and names[j][0] != "A" and names[j][0] != "R" and names[j][0] != "C" and names[j][0] != "H":
                    continue
                if names[k][0] != "M" and names[k][0] != "A" and names[k][0] != "R" and names[k][0] != "C" and names[k][0] != "H":
                    continue
                count += 1
    print(count)

if __name__ == '__main__':
    main()
