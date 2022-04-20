
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    l = []
    for i in range(n):
        l.append(sys.stdin.readline().rstrip())
    l2 = []
    for i in range(len(l)):
        if i < len(l)-1:
            if l[i][-1] == l[i+1][0]:
                l2.append(l[i+1])
            else:
                print("No")
                return
        if i == len(l)-1:
            if l[i] in l2:
                print("No")
                return
            else:
                print("Yes")
                return

if __name__ == "__main__":
    main()