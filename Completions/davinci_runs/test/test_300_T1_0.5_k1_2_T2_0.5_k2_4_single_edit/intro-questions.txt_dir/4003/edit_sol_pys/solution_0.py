
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
    int N, K;
    cin >> N >> K;
    vector<int> A(N, 0);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    int ans = 0;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if ((A[i] + A[j]) % K == 0)
            {
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}


n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = [a[0]]
    r = [a[n-1]]
    l_i = 1
    r_i = n-2
    while l_i < r_i:
        if a[l_i] > l[-1]:
            l.append(a[l_i])
            l_i += 1
        if a[r_i] > r[-1]:
            r.append(a[r_i])
            r_i -= 1
        if a[l_i] <= l[-1] and a[r_i] <= r[-1]:
            break
    if len(l) > len(r):
        print(len(l))
        print("L"*len(l))
    else:
        print(len(r))
        print("R"*len(r))
