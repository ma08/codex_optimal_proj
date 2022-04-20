
def main():
    n = int(input())  # 入力受け取り
    a = list(map(int, input().split()))  # 入力受け取り
    min_a = min(a)  # 最小値を求める
    max_a = max(a)  # 最大値を求める
    if min_a == max_a:  # 最小値と最大値が等しいか判定
        print("YES")  # 等しければYESを出力
    else:  # 最小値と最大値が等しくなければ
        print("NO")  # NOを出力

if __name__ == "__main__":
    main()
