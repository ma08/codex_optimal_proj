#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <bitset>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

import sys 
k, x = map(int, input().split())

for i in range(max(x - k + 1, -1000000), min(x + k, 1000000) + 1):
    print(i, end=' ')
