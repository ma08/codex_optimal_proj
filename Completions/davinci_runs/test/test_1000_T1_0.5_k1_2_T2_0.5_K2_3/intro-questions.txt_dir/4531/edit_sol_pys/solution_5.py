#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-01 15:09:56
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 1 of python challenge
# 
# 思路：先用Python的语法把字符串转换成对应的数字，再用Python的内建函数求和
#       再用Python的语法把数字转换成字符串，打印出来
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/def/0.html
#       3. next level url : http://www.pythonchallenge.com/pc/def/274877906944.html
#
import re


def get_sum(num_str):
    num_sum = 0
    for i in range(len(num_str)):
        num_sum += int(num_str[i])
    return num_sum

def get_str_from_num(num):
    return str(num)

def main():
    num_str = '1234567890'
    num_sum = get_sum(num_str)
    print(num_sum)
    num_str = get_str_from_num(num_sum)
    print(num_str)

edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))

adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)


def dfs(u, p):
    subtree_size_u = 1
    subtree_sum_u = a[u]
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v = dfs(v, u)
            subtree_size_u += subtree_size_v
            subtree_sum_u += subtree_sum_v
    return subtree_size_u, subtree_sum_u


def solve(u, p):
    subtree_size_u = 1
    subtree_sum_u = a[u]
    for v in adj[u]:
        if v != p:
            subtree_size_v, subtree_sum_v = dfs(v, u)
            subtree_size_u += subtree_size_v
            subtree_sum_u += subtree_sum_v
    max_cost = subtree_sum_u
    for v in adj[u]:
        if v != p:
            max_cost = max(max_cost, solve(v, u) + subtree_sum_u - subtree_sum_v)
    return max_cost


print(solve(0, -1))
