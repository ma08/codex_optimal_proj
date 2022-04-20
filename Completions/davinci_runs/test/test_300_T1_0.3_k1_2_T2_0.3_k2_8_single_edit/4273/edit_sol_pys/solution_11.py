

import sys

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = [i[0] for i in s if i[0] in ['M', 'A', 'R', 'C', 'H']] # リスト内包表記でM,A,R,C,Hの文字だけ取り出す
    s = list(set(s)) # 重複を消す
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6) # 順列の公式

if __name__ == '__main__':
    main()
