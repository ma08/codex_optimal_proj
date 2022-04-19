
import sys

def main():
    s = sys.stdin.readline().rstrip()
    count = 0
    for i in range(len(s) - 1):  # range(len(s) - 1)で、sの最後の文字は比較できないので、それ以外の文字数を指定
        if s[i] == s[i + 1]:  # s[i]とs[i + 1]を比較
            count += 1
    print(count)

if __name__ == '__main__':
    main()
