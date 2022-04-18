#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:39:28 2019

@author: suryakantkumar
"""

'''
Problem : Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. 
For example, if your string is "bcbc", you can either remove 'b' at index  or 'c' at index . If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Function Description : Complete the palindromeIndex function in the editor below. It must return the index of the character to remove or .
palindromeIndex has the following parameter(s):
s: a string to analyze

Input Format : The first line contains an integer , the number of queries. 
Each of the next  lines contains a query string .

Constraints : 
All characters are in the range ascii[a-z].

Output Format : Print an integer denoting the zero-indexed position of the character to remove to make  a palindrome. If  is already a palindrome or no such character exists, print .

Sample Input : 
3
aaab
baa
aaa

Sample Output : 
3
0
-1

'''

import os

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            if s[i] == s[len(s)-2-i]:
                return len(s)-1-i
            elif s[i+1] == s[len(s)-1-i]:
                return i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')
    fptr.close()

'''
# Other Solution

def solve(n, k, s):
    s = list(s)
    while k > 0:
        changed = False
        for i in range(n-1):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                k -= 1
                changed = True
                break
        if not changed:
            break
    return "".join(s)

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
'''
    print(solve(n, k, s))
