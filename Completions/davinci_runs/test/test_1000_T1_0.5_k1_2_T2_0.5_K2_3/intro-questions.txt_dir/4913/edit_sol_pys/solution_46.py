
import sys

def main():
    n = int(sys.stdin.readline().strip())
    vac = [0, 0, 0, 0]
    ctrl = [0, 0, 0, 0]
    for i in range(n):
        line = sys.stdin.readline().strip()
        if line[0] == 'Y':
            for j in range(4):
                if line[j] == 'Y':
                    vac[j-1] += 1
        else:
            for j in range(4):
                if line[j] == 'Y':
                    ctrl[j-1] += 1
    for i in range(4):
        if ctrl[i] == 0:
            print("Not Effective", end=" ")
        else:
            print("{:.6f}".format((vac[i]/ctrl[i])*100), end=" ")

if __name__ == "__main__":
    main()
