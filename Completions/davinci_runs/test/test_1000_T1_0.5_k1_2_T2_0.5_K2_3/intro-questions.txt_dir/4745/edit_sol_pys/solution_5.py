
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <functional>
#include <cmath>
#include <limits>
#include <list>
#include <memory>
#include <stack>
#include <iterator>
#include <queue>
#include <numeric>
#include <bitset>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;
#SOLUTION 
n, x = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

left = 0
right = n - 1

result = 0
while left < right:
    if prices[left] + prices[right] > x:
        result += 1
    right -= 1
    if prices[left] + prices[right] > x:
        result += 1
    left += 1

if left == right and prices[left] > x:
    result += 1

print(result)
