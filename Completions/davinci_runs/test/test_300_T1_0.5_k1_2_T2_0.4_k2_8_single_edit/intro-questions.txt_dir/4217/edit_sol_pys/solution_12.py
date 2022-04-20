

def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k = int(input().split()[0]) # 入力から食べる食べ物の数を取得
        for j in map(int, input().split()): # 入力から食べる食べ物の番号を取得
            foods[j-1] += 1
    print(foods.count(n))

if __name__ == '__main__':
    main()
