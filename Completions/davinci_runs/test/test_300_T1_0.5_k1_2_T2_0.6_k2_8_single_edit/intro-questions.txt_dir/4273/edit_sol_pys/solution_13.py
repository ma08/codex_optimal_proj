
import sys

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().strip() for _ in range(N)]  # n行の文字列を取得
    dic = {}
    for name in names:  # 各nameについて、最初の文字をkeyとして、辞書に登録する
        if name[0] in dic:
            dic[name[0]] += 1
        else:
            dic[name[0]] = 1
    keys = dic.keys()  # 辞書のキーをリストとして取得
    ans = 0
    for i in range(len(keys)):  # 辞書のキーを全て走査
        for j in range(i+1, len(keys)):  # i+1から最後まで走査
            for k in range(j+1, len(keys)):  # j+1から最後まで走査
                ans += dic[keys[i]] * dic[keys[j]] * dic[keys[k]]
    print(ans)


if __name__ == '__main__':
    main()
