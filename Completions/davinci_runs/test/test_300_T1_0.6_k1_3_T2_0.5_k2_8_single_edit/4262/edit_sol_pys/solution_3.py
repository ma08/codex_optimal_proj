
def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_order = 0
    q_order = 0
    for i in range(len(p)):  # 1~nまでの数を列挙
        p_order += p[i] - 1  # 小さい数から順にindexを加算
        q_order += q[i] - 1  # 小さい数から順にindexを加算
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:  # 小さい数から順にindexを加算
                p_order += 1  # 小さい数から順にindexを加算
            if q[i] > q[j]:  # 小さい数から順にindexを加算
                q_order += 1  # 小さい数から順にindexを加算
    print(abs(p_order - q_order))


if __name__ == '__main__':
    main()
