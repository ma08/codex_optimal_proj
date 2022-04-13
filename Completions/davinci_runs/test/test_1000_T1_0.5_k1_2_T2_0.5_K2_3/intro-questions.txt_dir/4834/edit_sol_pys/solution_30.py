# coding: utf-8


# In[ ]:

#N = 3
#times = [4, 1, 2]

times.sort()

totalTime = 0

for i in range(N):
    totalTime += sum(times[i:])

print(totalTime)
