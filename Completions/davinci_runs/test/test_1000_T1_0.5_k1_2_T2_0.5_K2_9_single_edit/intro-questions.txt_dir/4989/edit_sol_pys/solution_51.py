

def main():
    n = int(input())
    a = [int(i) for i in input().split()]  # input()で受け取った文字列を空白で区切ってint型にしてリストにする
    a.sort()
    a.reverse()
    alice = 0  # 各人の合計を入れる変数を用意
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice, bob)

main()
