

"""
解説
・解説見た
・問題文に書いてある通り、都市iは都道府県P_iに属し、その都道府県の中で第x番目に設立された都市ということ。
　つまり、都道府県P_iで、第x番目に設立された都市iに対して、都道府県P_iのIDと、xのIDをつけることになる。
・それぞれの都道府県で、設立された順にソートして、設立順にIDをつけていけばいい。
・設立された順にソートするのは、設立年Y_iでソートして、同じ設立年の都市は都道府県P_iでソートすればいい。
・これを実装すると、設立年Y_iでソートして、都道府県P_iでソートして、それを都道府県のそれぞれの都市の設立順にソートしていく。
・都道府県のそれぞれの都市の設立順にソートするのは、設立順にIDをつけていけばいい。
・それぞれの都道府県の都市を設立順にソートしていくのは、辞書型で実装した。
・これでO(MlogM)で終わる。
"""

import sys

def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        P, Y = map(int, input().split())
        cities.append((P, Y, i))
    cities.sort(key=lambda x:(x[0], x[1]))
    dic = {}
    for city in cities:
        if city[0] not in dic:
            dic[city[0]] = []
        dic[city[0]].append(city)
    for i in range(M):
        P = cities[i][0]
        Y = cities[i][1]
        idx = dic[P].index((P, Y, cities[i][2]))
        print("{0:06}{1:06}".format(P, idx+1))

if __name__ == '__main__':
    main()