

n, l = map(int, input().split())

flavors = [l+i for i in range(n)]
flavor_sum = sum(flavors)

flavor_sum -= 2*min(flavors)

print(flavor_sum)