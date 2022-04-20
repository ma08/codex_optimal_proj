
def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k = int(input().split()[0])
        for j in range(k):
            foods[int(input().split()[0]) - 1] += 1  # -1しているのは、入力が1から始まるから
    print(foods.count(n))

if __name__ == '__main__':
    main()
