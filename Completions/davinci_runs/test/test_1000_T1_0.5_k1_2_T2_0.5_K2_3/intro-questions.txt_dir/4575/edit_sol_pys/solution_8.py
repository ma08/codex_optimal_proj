#coding: utf-8

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X
for a in A: # aはチョコレートの大きさ
    n = D // a # nは1日に食べる回数
    ans += n + 1 

print(X)
