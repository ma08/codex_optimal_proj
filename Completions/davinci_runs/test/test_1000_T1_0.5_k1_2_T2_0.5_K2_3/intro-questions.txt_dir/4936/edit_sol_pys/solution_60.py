
import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()]
    max_temp = []
    for i in range(len(temp)-2):
        if len(temp) == 1:
            print(1, temp[0])
            return
        if len(temp) == 2:
            print(1, temp[0])
            return
        max_temp.append(max(temp[i], temp[i+1], temp[i+2]))
    index = max_temp.index(min(max_temp))
    print(index+1, max_temp[index])

if __name__ == '__main__':
    main()
