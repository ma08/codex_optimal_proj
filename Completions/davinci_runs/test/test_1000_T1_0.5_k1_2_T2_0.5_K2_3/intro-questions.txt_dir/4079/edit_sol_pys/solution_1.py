
#include <iostream>
using namespace std;
# Solution

n = int(input())

for i in range(n):
    s = input()
    ok = False
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = True
            break
    if len(s) != len(set(s)):
        ok = False
    print('Yes' if ok else 'No')
