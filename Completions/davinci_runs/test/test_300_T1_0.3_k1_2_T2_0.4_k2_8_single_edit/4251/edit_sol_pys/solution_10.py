
# Solution

def solve(n, m, a):
    a.sort(key=lambda x: x[0]) #時間でソート
    ans = 0
    for i in range(1, n): #1つ目と2つ目を比較
        ans = max(ans, a[i][0] - a[i-1][0]) #最大値を求める
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split()) #n,mを入力
    a = []
    for i in range(n): #n個の時間を入力
        a.append(list(map(int, input().split()))) #aに入力を追加
    print(solve(n, m, a)) #解答を出力
