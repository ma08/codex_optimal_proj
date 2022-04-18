
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;
# SOLUTION
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
for(int i = 0; i < n; i++)
    x[i] += v[i];
x.sort()
d = 0
for(int i = 0; i < n - 1; i++)
    d += x[i + 1] - x[i];
print(d)
