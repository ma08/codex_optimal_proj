


def main():
    n = int(input()) #次元
    x = list(map(int, input().split())) #位置
    x.sort() #位置の並び替え
    ans_min = 1 #最小は1
    ans_max = 1 #最大は1
    for i in range(1, n): #最小はx_i+1 != x_iである数が増えていく
        if x[i] != x[i - 1]: #x_i+1 != x_i
            ans_min += 1 #1増える
    if x[0] != 1: #最小は1
        ans_max += 1 #1増える
    if x[-1] != n: #最大はn
        ans_max += 1 #1増える
    print(ans_min, ans_max) #答えを出力


if __name__ == "__main__":
    main()
