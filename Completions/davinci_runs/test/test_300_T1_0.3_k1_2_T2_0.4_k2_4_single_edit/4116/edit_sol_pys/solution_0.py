
n = int(input())

for i in range(1, 10):
    if n % i == 0 and 1 <= n // i <= 9:  # n/iを整数で計算するために//を使う
        print("Yes")
        exit()

print("No")
