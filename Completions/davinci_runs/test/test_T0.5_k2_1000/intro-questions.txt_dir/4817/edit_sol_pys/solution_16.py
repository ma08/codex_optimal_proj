
import sys

def main():
    num = sys.stdin.readline().strip()
    num = list(num)
    for i in range(len(num) - 1, 0, -1):
        if num[i] > num[i - 1]:
            break
    else:
        print(0)
        return
    for j in range(len(num) - 1, i - 1, -1):
        if num[j] > num[i - 1]:
            break
    num[i - 1], num[j] = num[j], num[i - 1]
    num[i:] = sorted(num[i:])
    print(''.join(num))

if __name__ == '__main__':
    main()
