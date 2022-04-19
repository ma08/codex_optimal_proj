
import sys

def main():
    n = int(input())
    names = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if names[i][0] == names[j][0] == names[k][0]:
                    continue  # 同じ文字で始まる名前はダメ
                if names[i][0] not in "MARCH" or names[j][0] not in "MARCH" or names[k][0] not in "MARCH":
                    continue  # M,A,R,C,H以外で始まる名前はダメ
                count += 1  # ここまで来たらOK
    print(count)

if __name__ == '__main__':
    main()
