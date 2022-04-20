

def main():
    n = int(input())
    p = list(map(int, input().split()))  # 入力を受け取る
    q = list(map(int, input().split()))  # 入力を受け取る
    p_order = 0
    q_order = 0
    for i in range(len(p)):
        p_order += p[i]-1  # 順列の順番を計算
        q_order += q[i]-1  # 順列の順番を計算
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                p_order += 1  # 順列の順番を計算
            if q[i] > q[j]:
                q_order += 1  # 順列の順番を計算
    print(abs(p_order-q_order))

if __name__ == '__main__':
    main()
