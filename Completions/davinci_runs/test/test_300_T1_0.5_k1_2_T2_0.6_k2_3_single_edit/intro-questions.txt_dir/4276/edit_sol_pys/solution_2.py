#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#N個のレシピ

#T分以内で作れるレシピを探す
N, T = map(int, input().split())

#それぞれのレシピの料理時間
costs = []
#それぞれのレシピの料金
times = []
#各レシピを入力

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)
#T分以内に作れるレシピのみ抽出

#T分以内に作れるレシピが無い場合
costs = [costs[i] for i in range(len(costs)) if times[i] <= T]
    #TLE
if len(costs) == 0:
#T分以内に作れるレシピがある場合
    print('TLE')
else:
    print(min(costs))
