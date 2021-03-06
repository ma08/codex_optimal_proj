# 問題文
# N人の人が座ることができる席があります。
# 席は1からNまで番号がついています。
# i(1≦i≦N)番目の人は、席が空いているうちで、自分の席から最も近い席を選びます。(i番目の人は、席が空いているうちで、自分の席から最も近い席を選びます。)
# このとき、席が複数ある場合は、そのうちで席番号が最も小さい席を選びます。
# 例えば、席が空いているのは、席番号が3、5、7、9、11の5つの席であれば、席番号が3のものを選びます。
# このとき、席番号が3のものが選ばれたので、席番号が4のものは席が空いていないとみなします。
# このように、人が選んだ席を使った後は、その席から1つ右にある席も使ったものとみなします。
# このようにして、N人が席を選ぶとき、席が空いているものは何席でしょうか。
#
# 制約
# 1≦N≦100000
# 1≦Li≦Ri≦N
# Li≠Ri
# 入力はすべて整数である。
# 入力
# 入力は以下の形式で標準入力から与えられる。
#
# N
# L1 R1
# L2 R2
# :
# LN RN
# 1行目には、席の数を表す整数Nが与えられる。
# 続くN行には、それぞれの人が席を選ぶ範囲を表す整数Li,Riが空白区切りで与えられる。
# 出力
# 席が空いているものは何席でしょうか。(席が空いているものは何席でしょうか。)
#
# 入力例1
# 4
# 1 3
# 2 4
# 3 4
# 1 2
# 出力例1
# 2
# 入力例2
# 5
# 1 3
# 2 4
# 3 4
# 1 2
# 2 3
# 出力例2
# 3
# 入力例3
# 3
# 1 3
# 2 3
# 1 2
# 出力例3
# 1

N = int(input())
count = 0
seats = [0 for i in range(100000)]
for i in range(N):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        seats[j-1] += 1
for i in range(len(seats)):
    if seats[i] > 0:
        count += 1
print(count)
