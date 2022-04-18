
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <string>
#define lli long long int
#include <set>
#include <map>
#include <utility>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <sstream>
using namespace std;
#define MAX 100
#define INF 100000000
#define pi 3.141592653589793
#define e 2.718281828459045
#define mp make_pair
#define pb push_back
#define f first
#define s second
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int n;
    cin>>n;
    int a[n];
    for (int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int count=0;
    for (int i=0;i<n;i++)
    {
        if (a[i]%2==0)
        {
            count++;
        }
    }
    cout<<count<<endl;
}
# SOLUTION
m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]

def satisfiable(clauses, n):
    for clause in clauses:
        if clause[0] < 0:
            if clause[1] < 0:
                if clause[2] < 0:
                    return False
            else:
                if clause[2] > 0:
                    return False
        else:
            if clause[1] > 0:
                if clause[2] > 0:
                    return False
    return True

if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
