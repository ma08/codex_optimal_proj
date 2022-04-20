

n = int(input())
a_list = [int(i) for i in input().split()]

# 全部の要素を掛け算して、それぞれの最小公倍数を求める
lcm = 1
for i in a_list:
    lcm = (lcm * i) // math.gcd(lcm, i)

# 各要素の倍数を足していく
ans = 0
for i in a_list:
    ans += lcm // i

print(ans)