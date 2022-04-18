

import sys

def main():
    n = int(sys.stdin.readline().strip())
    vax = [0, 0, 0, 0]
    ctrl = [0, 0, 0, 0]
    for i in range(n):
        line = sys.stdin.readline().strip()
        if line[0] == 'Y':
            for j in range(4):
                if line[j+1] == 'Y':
                    vax[j] += 1
        else:
            for j in range(4):
                if line[j+1] == 'Y':
                    ctrl[j] += 1
    for i in range(4):
        if ctrl[i] == 0:
            print("Not Effective")
        else:
            print("{:.6f}".format((vax[i]/ctrl[i])*100))

if __name__ == "__main__":
    main()
