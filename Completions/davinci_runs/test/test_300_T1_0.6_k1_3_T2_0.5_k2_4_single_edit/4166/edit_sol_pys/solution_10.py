
# -*- coding: utf-8 -*-

# Copyright (c) 2019 fuyuno
# https://github.com/fuyuno/weekly-contest-101

N, M = map(int, input().split())
for i in range(10 ** N):
    if all(str(i).zfill(N)[s - 1] == str(c) for s, c in (map(int, input().split()) for _ in range(M))):
        print(i)
        exit()
print(-1)
