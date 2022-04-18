
import sys

def main():
    n = sys.stdin.readline().strip()
    if n == '0':
        print(0)
    else:
        temp = [int(i) for i in sys.stdin.readline().strip().split()]
        max_temp = []
        for i in range(len(temp) - 2):
            max_temp.append(max(temp[i], temp[i + 1], temp[i + 2]))
        index = max_temp.index(min(max_temp))
        print(index + 1, max_temp[index])


if __name__ == '__main__':
    main()
