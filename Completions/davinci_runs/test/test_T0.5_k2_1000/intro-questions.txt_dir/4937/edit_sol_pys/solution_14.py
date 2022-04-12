
import sys

def main():
    values = sys.stdin.readline().strip().split()
    n = int(values[0])
    a = int(values[1])
    values = sys.stdin.readline().strip().split()
    en = [int(i) for i in values]
    en.sort()
    en.reverse()
    result = 0
    for i in range(n):
        if a > en[i]:
            a -= en[i]
            result += 1
        else:
            break
    print(result)

if __name__ == "__main__":
    main()
