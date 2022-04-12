
N, L = map(int, input().split())
apple_flavors = [L + i for i in range(N)]  # 苹果的口味
apple_flavors.remove(max(apple_flavors))  # 去掉最苦的苹果
print(sum(apple_flavors))
