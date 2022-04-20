
import sys

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if names[i][0] != names[j][0] and names[i][0] != names[k][0] and names[j][0] != names[k][0]:
                    if names[i][0] == "M" or names[i][0] == "A" or names[i][0] == "R" or names[i][0] == "C" or names[i][0] == "H":
                        if names[j][0] == "M" or names[j][0] == "A" or names[j][0] == "R" or names[j][0] == "C" or names[j][0] == "H":
                            if names[k][0] == "M" or names[k][0] == "A" or names[k][0] == "R" or names[k][0] == "C" or names[k][0] == "H":
                                count += 1
    print(count)

if __name__ == '__main__':
    main()
