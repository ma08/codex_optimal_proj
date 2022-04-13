# ABC081A
n = input()
print(n.count("1"))


# ABC081B

n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))  # list()でリスト化しておく

count = 0
while all(a % 2 == 0 for a in a_list):  # すべて偶数かどうか
    a_list = [a / 2 for a in a_list]  # for文の中でリスト内包表記を使う
    count += 1

cost = 0
for i in a_list:
    if i >= x:
        cost += 1  # リストa_list内の要素がx以上ならcostに1足す

print(cost)
