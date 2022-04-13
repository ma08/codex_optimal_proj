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

if count >= x:
    print(count)
else:
    for i in range(x, n + 1):
        if i in a_list:
            cost += 1

    print(cost)
