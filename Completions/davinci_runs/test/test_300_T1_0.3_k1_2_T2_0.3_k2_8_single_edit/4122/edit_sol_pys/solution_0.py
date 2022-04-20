
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <numeric>
#include <set>
#include <list>
#include <bitset>
#include <cstdlib>
#include <map>
using ll = long long int;
using namespace std;

int main()
{
    int H, n;
    cin >> H >> n;
    vector<int> d(n);
    for (int i = 0; i < n; i++)
    {
        cin >> d[i];
    }

H, n = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
