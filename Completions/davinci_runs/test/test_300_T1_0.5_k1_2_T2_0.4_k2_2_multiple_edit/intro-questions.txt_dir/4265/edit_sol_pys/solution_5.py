

import sys

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1  # sとtで異なる文字がある場合、カウントを1つ増やす
    print(count)

if __name__ == '__main__':
    main()
