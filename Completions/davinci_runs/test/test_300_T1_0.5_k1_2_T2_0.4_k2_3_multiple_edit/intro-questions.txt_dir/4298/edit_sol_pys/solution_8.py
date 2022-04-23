
import math

def main():
    N, D = map(int, input().split())  # N: 全体の人数, D: 手渡しする人数
    print(math.ceil((N - D) / (2 * D + 1)) + 1)  # 回数

if __name__ == "__main__":
    main()
