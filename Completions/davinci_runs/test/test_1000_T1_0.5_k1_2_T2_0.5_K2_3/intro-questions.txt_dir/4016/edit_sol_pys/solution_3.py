
def main():
    n, k = map(int, input().split())
    t = input()
    print(t*(k//n) + t[:k%n])  # 切り上げは// 


if __name__ == "__main__":
    main()
