
import sys

def main():
    n = int(sys.stdin.readline().strip())
    vax = [0, 0]
    ctrl = [0, 0]
    for i in range(n):
        line = sys.stdin.readline().strip()
        for j in range(2):
            if line[j] == 'Y':
                if line[-1] == 'Y':
                    vax[j] += 1
                else:
                    ctrl[j] += 1
    for i in range(2):
        if ctrl[i] == 0:
            print("Not Effective")
        else:
            print("{:.6f}".format((vax[i]/ctrl[i])*100))

if __name__ == "__main__":
    main()
