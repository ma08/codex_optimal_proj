

N, L = map(int, input().split())

taste_list = [L + i for i in range(N)]

taste_list.remove(max(taste_list))

print(sum(taste_list))
