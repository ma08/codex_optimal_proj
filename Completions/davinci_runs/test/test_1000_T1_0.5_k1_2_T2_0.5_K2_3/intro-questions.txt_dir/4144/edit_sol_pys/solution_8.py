
import sys


# 各桁の和が10になるような数の総和を求める
# 各桁の和が10になるような数は、
# 1の位が1であり、それ以外の桁の和が9になるような数
# 1の位が2であり、それ以外の桁の和が8になるような数
# ...
# 1の位が9であり、それ以外の桁の和が1になるような数
# これらの数を9通り全て求める
# それぞれの数を、それ以外の桁が1桁である数と2桁以上の数に分ける
# 1桁の数は、それぞれの桁を1~9とすることができるので、
# 各桁について、1~9の9通り全てを求める
# 2桁以上の数は、各桁の和が9であるような数の総和を求める
# これは、各桁の和が10であるような数の総和から、1の位が9であるような数の総和を引くことで求めることができる
# これは、再帰関数で実装することができる
# 再帰関数の引数として、残りの桁数と、各桁の和が9になるような数を求めるための変数を渡す
# これらの引数は、再帰関数の中で、
# 残りの桁数が1である場合は、各桁の和が9になるような数の総和を1とする
# 残りの桁数が1でない場合は、
# 各桁の和が9になるような数の総和に、次の桁が1である場合と、次の桁が1でない場合の2通りを足したものを設定する
# これにより、各桁の和が9になるような数の総和を求めることができる

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(s, n):
    if s >= 10:
        return 0
    if n == 1:
        return 1
    res = dfs(s + 1, n - 1) + dfs(s, n - 1)
    return res % MOD


def solve():
    return dfs(1, N - 1) * 2 % MOD


print(solve())
